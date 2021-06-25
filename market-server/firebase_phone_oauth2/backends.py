from django.conf import settings
from django.contrib.auth.models import User
from oauthlib.oauth2.rfc6749 import errors
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from api.models import Profile, Tester, TestPhoneNumber, TempProfile
import logging, os

logger = logging.getLogger(__name__)

PROVIDER_EMAIL = 'password'
PROVIDER_PHONE = 'phone'


class FirebaseAuth():
    def do_auth(self, decode_token, temp_id):
        uid = decode_token['uid']
        sign_in_provider = decode_token['firebase']['sign_in_provider']
        try:
            # 기존 유저 (재발급 혹은 앱 재설치)
            user = User.objects.get(username=uid)
        except ObjectDoesNotExist:
            if sign_in_provider == PROVIDER_PHONE:
                phone_number = decode_token['phone_number']
                # 앱 사용자 중 연락처 업로드에 의해 생긴 프로필
                matched_profiles = Profile.objects.filter(phone_number=phone_number).select_related('owner').order_by(
                    "-id")[:1]
            else:
                return

            if len(matched_profiles) > 0:
                p = matched_profiles[0]
                user = p.owner
                user.username = uid
                user.save()
            else:
                # 신규유저
                user = User(username=uid)
                user.save()

                try:
                    print('enter add tester')
                    tp = TestPhoneNumber.objects.get(phone_number=decode_token['phone_number'])
                    Tester(
                        user=user,
                        phone_number=tp
                    ).save()
                    print('save tester')
                except:
                    print('exception add tester')
                    pass

        profile = user.profile
        profile.is_app_user = True

        # Todo : temp_id로 TempProfile 관련 작업필요.
        if temp_id:
            try:
                temp_profile = TempProfile.objects.get(id=temp_id)
                profile.app_version = temp_profile.app_version
                profile.platform = temp_profile.platform
                profile.service_terms = temp_profile.service_terms
                profile.privacy_terms = temp_profile.privacy_terms
                profile.location_terms = temp_profile.location_terms
            except TempProfile.DoesNotExist as e:
                pass

        if sign_in_provider == PROVIDER_PHONE:
            profile.phone_number = decode_token['phone_number']
        else:
            pass
        profile.save()

        return user
