from django.db.models import Q

from models import User



class AccountManage:

	@classmethod
	async def get_user(cls, id):
		try:
			return await User.objects.aget(Q(id=id) | Q(username=id))

		except User.DoesNotExist:
			return None