# Interface Segregation Principle (ISP) - принцип разделения интерфейсов.
# Лучше иметь много небольших, чем иметь один большой интерфейс.


# wrong
class Machine:
    def print_document(self):
        pass

    def scan_document(self):
        pass

    def fax_document(self):
        pass

    def cancel_printing(self):
        pass


class MultiFunctionPrinter(Machine):
    def print_document(self):
        print("Printing document")

    def scan_document(self):
        print("Scanning document")

    def fax_document(self):
        print("Faxing document")

    def cancel_printing(self):
        print("Cancelling...")


class OldFashionedPrinter(Machine):
    def print_document(self):
        print("Printing document")

    def scan_document(self):
        # Old fashioned printers cannot scan documents
        raise NotImplementedError

    def fax_document(self):
        # Old fashioned printers cannot fax documents
        raise NotImplementedError

    def cancel_printing(self):
        # Old fashioned printers cannot fax documents
        raise NotImplementedError


# correct
class Printable:
    def print(self):
        pass


class Editable:
    def edit(self):
        pass


class Document(Printable, Editable):
    def print(self):
        print("Printing document")

    def edit(self):
        print("Editing document")


def print_document(printable: Printable):
    printable.print()


if __name__ == '__main__':
    document = Document()
    print_document(document)  # prints "Printing document"
