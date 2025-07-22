#Jeremy Durdel
#Chapter 15 Lab 1
#07/21/2025

from dataclasses import dataclass

@dataclass
class Employee:
    __name: str
    __hours_worked: float
    __hourly_rate: float

    @property
    def name(self):
        return self.__name

    @property
    def calc_pay(self):
        return self.__hours_worked * self.__hourly_rate

@dataclass
class Salesperson(Employee):
    __weekly_sales: float
    __commission_rate: float

    @property
    def calc_pay(self) -> float:
        base = super().calc_pay
        commission = self.__weekly_sales * self.__commission_rate
        return base + commission