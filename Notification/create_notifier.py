from types import MethodType

# Attaches to class instances
def attach_notifier(obj, notifying_methods = []):
    # Add attributes for handling and notifying observers
    obj.observers = []
    obj.notify = MethodType(notify, obj)
    obj.attach = MethodType(attach, obj)
    obj.detach = MethodType(detach, obj)

    # Wrap methods to trigger notification
    for method in notifying_methods:
        if hasattr(obj, method.__name__):
            unwrapped = getattr(obj, method.__name__)
            def wrapped(self, *args, __unwrapped=unwrapped, **kwargs):
                result = __unwrapped(*args, **kwargs)
                self.notify()
                return result
            setattr(obj, method.__name__, MethodType(wrapped, obj))


def notify(self):
    print("Notified")
    for observer in self.observers:
        observer.update(self)

def attach(self, observer):
    print("Attached")
    self.observers.append(observer)

def detach(self, observer):
    print("Detached")
    self.observers.remove(observer)
