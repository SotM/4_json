# Prettify JSON

������� �� ���� ������� JSON ����, � �� ������ �������� ����������� ������ �����.

# Quickstart

[TODO]

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>
[
    {
        "Id": "79742784-9ef3-4543-bc98-a219a8903c18",
        "Number": 1,
        "Cells": {
            "global_id": 14371450,
            "Name": "��������� ���",
            "IsNetObject": "��",
            "OperatingCompany": "��������� ���",
            "TypeService": "���������� ����������������� �������",
            "AdmArea": "�������� ���������������� �����",
            "District": "����� �������",
            "Address": "����� ��������� �������, ��� 10",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ],
            "WorkingHours": [
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "�����������"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "�������"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "�����"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "�������"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "�������"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "�������"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "�����������"
                }
            ],
            "ClarificationOfWorkingHours": null,
            "geoData": {
                "type": "Point",
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ]
            }
        }
    },
    {
        "Id": "1bd07c21-05de-4015-b015-d22657168ded",
        "Number": 2,
        "Cells": {
            "global_id": 14934782,
            "Name": "��������� � ���������",
            "IsNetObject": "��",
            "OperatingCompany": "���������",
            "TypeService": "���������� ����������������� �������",
            "AdmArea": "������-��������� ���������������� �����",
            "District": "����� ��������",
            "Address": "����� �������, ��� 6",
            "PublicPhone": [
                {
                    "PublicPhone": "(499) 909-40-08"
                }
            ],
            "WorkingHours": [
                {
                    "Hours": "10:00-22:00",
                    "DayOfWeek": "�����������"
                },
                {
                    "Hours": "10:00-22:00",
                    "DayOfWeek": "�������"
                },
                {
                    "Hours": "10:00-22:00",
                    "DayOfWeek": "�����"
                },
                {
                    "Hours": "10:00-22:00",
                    "DayOfWeek": "�������"
                },
                {
                    "Hours": "10:00-22:00",
                    "DayOfWeek": "�������"
                },
                {
                    "Hours": "10:00-22:00",
                    "DayOfWeek": "�������"
                },
                {
                    "Hours": "10:00-22:00",
                    "DayOfWeek": "�����������"
                }
            ],
            "ClarificationOfWorkingHours": null,
            "geoData": {
                "type": "Point",
                "coordinates": [
                    37.59317706430676,
                    55.89772236936797
                ]
            }
        }
    },
    {
        "Id": "a16c8154-09d8-4207-8e13-cb8db654e95c",
        "Number": 3,
        "Cells": {
            "global_id": 14937274,
            "Name": "������-�",
            "IsNetObject": "���",
            "OperatingCompany": null,
            "TypeService": "���������� ����������������� �������",
            "AdmArea": "������-��������� ���������������� �����",
            "District": "����� ��������",
            "Address": "������������ �����, ��� 72",
            "PublicPhone": [
                {
                    "PublicPhone": "(905) 791-87-13"
                }
            ],
            "WorkingHours": [
                {
                    "Hours": "09:00-22:00",
                    "DayOfWeek": "�����������"
                },
                {
                    "Hours": "09:00-22:00",
                    "DayOfWeek": "�������"
                },
                {
                    "Hours": "09:00-22:00",
                    "DayOfWeek": "�����"
                },
                {
                    "Hours": "09:00-22:00",
                    "DayOfWeek": "�������"
                },
                {
                    "Hours": "09:00-22:00",
                    "DayOfWeek": "�������"
                },
                {
                    "Hours": "09:00-22:00",
                    "DayOfWeek": "�������"
                },
                {
                    "Hours": "09:00-22:00",
                    "DayOfWeek": "�����������"
                }
            ],
            "ClarificationOfWorkingHours": null,
            "geoData": {
                "type": "Point",
                "coordinates": [
                    37.58803599964753,
                    55.89020100016689
                ]
            }
        }
    }
]

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
