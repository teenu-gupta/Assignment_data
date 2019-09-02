import sys
import os
import django
import csv
import datetime
from analysis.models import BusinessDetail

sys.path.append("C:\\Users\\teenu.gupta\\Desktop\\ff\\final")
# Set it to the root of your project
os.environ["DJANGO_SETTINGS_MODULE"] = "myproject.settings"
django.setup()


def convert_datetime(val):
    if val != "NULL":
        return datetime.datetime.strptime(val, "%Y-%m-%d %H:%M:%S")
    else:
        return ''


def convert_date(val):
    if val != "NULL":
        return datetime.datetime.strptime(val, "%Y-%m-%d %H:%M:%S")
    else:
        return ''


def open_file(path):
    """
    Open and read an Excel file
    """
    # book = pd.read_csv(path, delimiter="\t")
    # book = xlrd.open_workbook(path)
    with open(path, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")
        i =0
        for row in csv_reader:
            # import pdb;pdb.set_trace()
            print row
            if i == 0:
                i = i + 1
                continue
            data = {"account_state": row[0],
                    "account_id": row[1],
                    "plan_name": row[6],
                    "business_id": row[7],
                    "enterprise_id": row[8],
                    "category_id" : row[10],
                    "parent_category_name": row[11],
                    "count": row[12],
                    "avg_monthly_rating": float(row[13])
                    }

            data["activated_at"] = convert_datetime(row[2])
            data["expires_at"] = convert_date(row[3])
            data["current_period_started_at"] = convert_datetime(row[4])
            data["current_period_ends_at"] = convert_datetime(row[5])
            data["created"] = convert_datetime(row[9])
            try:
                business_data, created = BusinessDetail.objects.get_or_create(**data)
                business_data.save()
            except Exception as e:
                print e.message
                print "the example row is  %s ", str(row)
                pass


path = raw_input("Please enter path of your file: ")
print "************************************************Started***********************************************"
open_file(path)
print "************************************************Completed*********************************************"

