# Delete a Book instance

>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
(1, {'bookshelf.Book': 1})
# Output confirms one record was deleted.

>>> Book.objects.all()
<QuerySet []>
# No books left in the database.
