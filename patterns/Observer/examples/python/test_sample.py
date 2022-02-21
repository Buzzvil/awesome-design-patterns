from sample import GalaxyObserver, IPhoneObserver, PhoneStore, NONE_STATE


def test_phone_store() -> None:
    subject = PhoneStore()

    iphone_observer = IPhoneObserver()
    subject.attach(iphone_observer)

    galaxy_observer = GalaxyObserver()
    subject.attach(galaxy_observer)

    subject.update_state("Galaxy 7")
    assert iphone_observer.last_notified_state == NONE_STATE
    assert galaxy_observer.last_notified_state == "Galaxy 7"

    subject.update_state("IPhone 8+")
    assert iphone_observer.last_notified_state == "IPhone 8+"
    assert galaxy_observer.last_notified_state == "Galaxy 7"

    subject.detach(iphone_observer)

    subject.update_state("IPhone X")
    assert iphone_observer.last_notified_state == "IPhone 8+"
    assert galaxy_observer.last_notified_state == "Galaxy 7"
