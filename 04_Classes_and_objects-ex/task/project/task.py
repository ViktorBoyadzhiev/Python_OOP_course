from typing import List


class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments: List[str] = []
        self.completed = False

    def change_name(self, new_name):
        if self.name == new_name:
            return "Name cannot be the same."

        self.name = new_name

        return new_name

    def change_due_date(self, new_due_date):
        if self.due_date == new_due_date:
            return "Date cannot be the same."

        self.due_date = new_due_date

        return new_due_date

    def add_comment(self, comment: str) -> None:
        self.comments.append(comment)

    def edit_comment(self, comment_index: int, new_comment: str) -> str:
        if not 0 <= comment_index < len(self.comments):
            return "Cannot find comment"

        self.comments[comment_index] = new_comment

        return ', '.join(self.comments)

    def details(self) -> str:
        return f"Name: {self.name} - Due Date: {self.due_date}"