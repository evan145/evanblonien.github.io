import {
  startOfWeek,
  addDays,
  startOfMonth,
  endOfMonth,
  endOfWeek,
  isSameMonth,
  isSameDay,
  getYear,
  format,
  addMonths,
  subMonths,
  eachYearOfInterval,
} from "date-fns";
import { FastCalendarDay } from "./fast-calendar-day";

export class FastCalendar {
  private readonly daysPerWeek = 7;
  private readonly weeksPerMonth = 5;

  private date!: Date;
  private _selectedDate: Date | undefined;
  private _year!: string;
  private _yearShort!: string;
  private _month!: string;
  private _monthShort!: string;
  private _days: FastCalendarDay[] = [];

  constructor({ date = new Date() }: { date?: Date } = {}) {
    this.setDate({
      year: date.getFullYear(),
      month: date.getMonth(),
      day: date.getDate(),
    });
    this.generateCalendar();
  }

  get selectedDate() {
    return this._selectedDate;
  }

  get year() {
    return this._year;
  }

  get yearShort() {
    return this._yearShort;
  }

  get month() {
    return this._month;
  }

  get monthShort() {
    return this._monthShort;
  }

  get days() {
    return this._days;
  }

  setDate({
    year,
    month,
    day = 1,
  }: {
    year: number;
    month: number;
    day?: number;
  }) {
    this.date = new Date(year, month, day);
    this.generateCalendar();
  }

  prevMonth() {
    this.date = subMonths(this.date, 1);
    this.generateCalendar();
  }

  nextMonth() {
    this.date = addMonths(this.date, 1);
    this.generateCalendar();
  }

  setSelectedDate({ date }: { date: Date }) {
    this._selectedDate = date;
    this.generateCalendar();
  }

  getWeekDays({ short = false }: { short?: boolean } = {}): string[] {
    const weekDays = [
      "Sunday",
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
    ];
    return short ? weekDays.map((wday) => wday.slice(0, 3)) : weekDays;
  }

  getMonths({ short = false }: { short?: boolean } = {}): string[] {
    const months = [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ];
    return short ? months.map((month) => month.slice(0, 3)) : months;
  }

  getYears({
    startYear,
    endYear,
    short,
  }: {
    startYear: number | string;
    endYear: number | string;
    short?: boolean;
  }): string[] {
    const start = new Date().setFullYear(+startYear);
    const end = new Date().setFullYear(+endYear);
    const years = eachYearOfInterval({ start, end }).map((date) =>
      date.getFullYear().toString()
    );
    return short ? years.map((month) => month.slice(-2)) : years;
  }

  private generateCalendar() {
    this._year = getYear(this.date).toString();
    this._yearShort = format(this.date, "yy");
    this._month = format(this.date, "MMMM");
    this._monthShort = format(this.date, "MMM");
    this._days = this.generateDays(this.date).slice(
      0,
      this.daysPerWeek * this.weeksPerMonth
    );
  }

  private generateDays(date: Date): FastCalendarDay[] {
    const startOfTheMonth = startOfMonth(date);
    const endOfTheMonth = endOfMonth(date);
    const startDate = startOfWeek(startOfTheMonth);
    const endDate = endOfWeek(endOfTheMonth);
    const days: FastCalendarDay[] = [];

    let currentDate = startDate;

    while (currentDate <= endDate) {
      days.push({
        date: currentDate,
        day: currentDate.getDate(),
        isSameMonth: isSameMonth(currentDate, date),
        isToday: isSameDay(currentDate, new Date()),
        isSelected:
          (this._selectedDate && isSameDay(currentDate, this._selectedDate)) ||
          false,
      });
      currentDate = addDays(currentDate, 1);
    }

    return days;
  }
}
