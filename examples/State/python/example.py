from abc import ABCMeta, abstractmethod


class TennisCourtState(metaclass=ABCMeta):
    @abstractmethod
    def reserve(self, member_id: str):
        pass

    @abstractmethod
    def pay(self, member_id: str):
        pass

    @abstractmethod
    def cancel(self, member_id: str):
        pass


class TennisCourtSystem:
    def __init__(self):
        self.current_state = FreeState(self)

    def reserve(self, member_id: str):
        self.current_state.reserve(member_id)

    def pay(self, member_id: str):
        self.current_state.pay(member_id)

    def cancel(self, member_id: str):
        self.current_state.cancel(member_id)

    def change_state(self, state: TennisCourtState):
        self.current_state = state


class FreeState(TennisCourtState):
    def __init__(self, system: TennisCourtSystem):
        self.system = system

    def reserve(self, member_id: str):
        print(f"{member_id}님으로 예약을 진행합니다. 결제가 필요합니다.")
        self.system.change_state(InProgressState(self.system, member_id))

    def pay(self, member_id: str):
        print(f"{member_id}님이 예약 진행중인 코트가 아니므로 결제할 수 없습니다.")

    def cancel(self, member_id: str):
        print(f"{member_id}님이 코트가 아니므로 취소할 수 없습니다.")


class InProgressState(TennisCourtState):
    def __init__(self, system: TennisCourtSystem, reserved_by: str):
        self.system = system
        self.reserved_by = reserved_by

    def reserve(self, member_id: str):
        print("다른 예약이 진행중이라 예약이 불가능합니다.")

    def pay(self, member_id: str):
        if member_id == self.reserved_by:
            print(f"결제되었습니다. {member_id}님의 예약이 완료되었습니다.")
            self.system.change_state(ReservedState(self.system, member_id))
        else:
            print("예약한 본인만 결제가 가능합니다.")

    def cancel(self, member_id: str):
        print(f"{member_id}님이 예약하신 코트가 아니므로 취소할 수 없습니다.")


class ReservedState(TennisCourtState):
    def __init__(self, system: TennisCourtSystem, reserved_by: str):
        self.system = system
        self.reserved_by = reserved_by

    def reserve(self, member_id: str):
        print("이미 예약된 코트입니다.")

    def pay(self, member_id: str):
        print("이미 예약된 코트입니다.")

    def cancel(self, member_id: str):
        if self.reserved_by == member_id:
            print(f"{member_id}님의 예약이 취소되었습니다.")
            self.system.change_state(FreeState(self.system))
        else:
            print(f"{member_id}님이 예약하신 코트가 아니므로 취소할 수 없습니다.")


if __name__ == '__main__':
    system = TennisCourtSystem()

    system.reserve('tennis_lover')
    system.reserve('annonymous')

    system.pay('tennis_lover')
    system.pay('annonymous')

    system.cancel('tennis_lover')
    system.reserve('annonymous')

    '''
    tennis_lover님으로 예약을 진행합니다. 결제가 필요합니다.
    다른 예약이 진행중이라 예약이 불가능합니다.
    
    결제되었습니다. tennis_lover님의 예약이 완료되었습니다.
    이미 예약된 코트입니다.
    
    tennis_lover님의 예약이 취소되었습니다.
    annonymous님으로 예약을 진행합니다. 결제가 필요합니다.
    
    '''
