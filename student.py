from dataclasses import dataclass


@dataclass
class Student:
    name: str
    college_id: int
    gpa: float

# normal class would look like this:
# class Student:
#     def __init__(self, name, college_id, gpa):
#         self.name = name
#         self.college_id = college_id
#         self.gpa = gpa
#
# far less boilerplate/syntactic sugar with dataclasses
# plus, dataclasses automatically get their own dunder methods (__str__,
# __eq__, etc.)


def main():
    alice = Student('Alice', 12345, 3.4)
    bob = Student('Bob', 98765, 3.22)

    print(alice)
    print(bob)

    # individual fields
    print(alice.gpa)
    print(bob.college_id)



main()
