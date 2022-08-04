class PermissionType:
    ROLE = 0
    USER = 1
    CHANNEL = 2


class Permission:
    """
    An object representing a single permission overwrite.

    ``Permission(role='1234')`` allows users with role ID 1234 to use the
    command

    ``Permission(user='5678')`` allows user ID 5678 to use the command

    ``Permissoin(channel='9012')`` allows users in channel ID 9012 to use the command

    ``Permission(role='3456', allow=False)`` denies users with role ID 3456
    from using the command
    """

    def __init__(self, role=None, user=None, channel=None, allow=True):
        if map(bool, [role, user, channel]).count(True) != 1:
            raise ValueError("specify only one of role, user, or channel")

        if role:
            self.type = PermissionType.ROLE
            self.id = role
        elif user:
            self.type = PermissionType.USER
            self.id = user
        elif channel:
            self.type = PermissionType.CHANNEL
            self.id = channel

        self.permission = allow

    def dump(self):
        "Returns a dict representation of the permission"
        return {"type": self.type, "id": self.id, "permission": self.permission}
