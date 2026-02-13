# Fast Calendar

Javascript library to help you create HTML calendars, make it easy to build calendars using any styles framework like Bootstrap, Tailwind, etc.

```javascript

February 2023
Sun, Mon Tue, Wed, Thu, Fri, Sat
[29, 30, 31, 1, 2, 3, 4,
 5, 6, 7, 8, 9, 10, 11,
 12, 13, 14, 15, 16, 17, 18,
 19, 20, 21, 22, 23, 24, 25,
 26, 27, 28, 1, 2, 3, 4]
```

### Install

```bash
npm install https://github.com/marco-martins/fast-calendar.git
# Note: Soon it will be published on NPMJS
```

### Basic usage

```javascript
import { FastCalendar } from 'fast-calendar';

// generating a calendar for the current month
const date = new Date('2023-02-11'):
const calendar = new FastCalendar({ date });
// optional mark a day as selected
const selectedDate = new Date('2023-02-12');
calendar.setSelectedDate(selectedDate);

// calendar object
{
  selectedDate: undefined;
  year: "2023";
  yearShort: "23";
  month: "February";
  monthShort: "Feb";
  days: [
    {
      date: 'Sun Jan 29 2023 01:00:00 GMT+0100', // native js date object
      day: 29,
      isSameMonth: false,
      isToday: false,
      isSelected: false,
    },
    ...
    {
      date: 'Sat Feb 11 2023 01:00:00 GMT+0100',
      day: 11,
      isSameMonth: true, // day out of the current calendar
      isToday: false,
      isSelected: false,
    },
    {
      date: 'Sun Feb 12 2023 01:00:00 GMT+0100',
      day: 12,
      isSameMonth: true,
      isToday: false,
      isSelected: true, // day marked as selected
    },
    ...
    {
      date: 'Sat Mar 04 2023 01:00:00 GMT+0100 ',
      day: 4,
      isSameMonth: false,
      isToday: false,
      isSelected: false,
    }]
  ]
}
```

### Methods

| Method          | Params                                                          | Description                                                                                                          |
| --------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| setDate()       | { year: number, month: number, day?: number }                   | Allow you to rebuild the calendar to a specific date                                                                 |
| setSelectedDate | { date: Date }                                                  | Allow you to set a day as selected, the correspondent day comes marked as isSelected (true)                          |
| prevMonth()     |                                                                 | Rebuild the calendar to the previews month                                                                           |
| nextMonth()     |                                                                 | Rebuild the calendar to the next month                                                                               |
| getWeekDays()   | { short?: boolean }                                             | Returns an array with day names ["Sunday", "Monday", "Tuesday", ...], short option to ["Sun", "Mon", "Tue", ...]     |
| getMonths()     | { short?: boolean }                                             | Returns an array with months names ["January", "February", "March", ...], short option to ["Jan", "Feb", "Mar", ...] |
| getYears()      | { startYear: number, endYear: number, string; short?: boolean } | Returns an array with years based on the range passed ["2018", ..., "2023"] short option to ["18", ..., "23"]        |

#### Contributions

```
Clone repo:
git clone git@github.com:marco-martins/fast-calendar.git

Build:
npm run build

Run the tests:
npm run test
```

#### TODO

- Remove date-fns dependency
- Support multi-language
