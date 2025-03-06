
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    
    def __init__(self, last_name):
        self.last_name = last_name    

        # example list of members
        self.members = [
            {
                "id": 1,
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": 2,
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": 3,
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
           
            ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if "id" not in member or member["id"] is None:
            member["id"] = self._generateId()
        if "last_name" not in member:
            member["last_name"] = self.last_name
        self.members.append(member)
        return member

    def delete_member(self, id):
        self.members = [m for m in self.members if m["id"] != id]
        return self.members

    def get_member(self, id):
        for member in self.members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        return self.members
