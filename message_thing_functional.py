import os
import csv
import json
import datetime
from matplotlib import pyplot as plt
import numpy as np



# CONSTANTS

# feel free to (please) change to fit your specific data better
# to change what graph you're actually generating, go to line 203

# if you know certain user/channel ids correspond to certain messages (by manually searching...)
# you can add them to the dictionary here in the given format
NAMES = {
         "885919856472514583": "nick",
         "700903472706355210": "melon",
         "952287968150827058": "josh",
         #"904633511540064266": "annli",
         "772312453702746133": "xe",
         "808761775217836032": "abi",
         "766492323613507640": "amogus",
         "638448921881870385": "david",
         "633478709470429204": "huxley",
         "886295169253646357": "selina",
         "783789099587731456": "jack",
         "624823252283424818": "albert",
         "904759432423022622": "dante",
         "754540884330283118": "old friend abi",
         "758552720185098261": "ow hours"}

# primary timezone you message in, not accounting for daylight savings, given in UTC time (pacific = -8)
TIMEZONE = -8

# theshold for number of messages you want with a user/channel for them to be graphed
# i message way too much so i use 1500, you might want to lower that to see more interesting things
THRESHOLD = 500

# cycle of colors used when plotting multiple lines
# to add to or ammend this list, go to https://matplotlib.org/stable/gallery/color/named_colors.html for named colors
COLORS = ["firebrick",
          "orangered",
          "orange",
          "gold",
          "yellowgreen",
          "forestgreen",
          "lightseagreen",
          "royalblue",
          "mediumblue",
          "purple",
          "mediumorchid",
          "violet",
          "deeppink"]




# DON'T TOUCH THIS PART OF THE CODE, GO TO LINE 203

# parse csv file
def parse_csv(file_path):
    with open(file_path, "r", encoding="utf8") as f:
        readCSV = csv.reader(f, delimiter=',')
        return list(readCSV)

# get the ids of all message channels in the "messages" folder
def get_message_channels():
    print("Loading channels...")
    message_channels = [x[0] for x in os.walk("messages") if not x[0] == "messages"]
    print("Loaded {} channels.".format(len(message_channels)))
    return message_channels

# reads all message data and returns two arrays of equal length
# first one of the user/channel ids and
# second a 2D array of all message dates corresponding to each user/channel
def get_dates_by_id(message_channels):
    print("Loading messages...")
    ids = []
    message_dates = []
    message_count = 0
    for channel in message_channels:
        f = open(channel + "/channel.json")
        data = json.load(f)
        ids.append(data["id"])
        messages = parse_csv(channel + "/messages.csv")
        dates = []
        for i in range(1,len(messages)):
            d = messages[i][1][:10]
            date = datetime.datetime.strptime(d, '%Y-%m-%d')
            dates.append(date)
            message_count += 1
        message_dates.append(dates)
    print("Loaded {} messages.".format(message_count))
    return ids, message_dates

# reads all message data and returns arrays of all hours, as well all dates messages were sent at
# input main timezone in utc, default set to pacific time (no daylight savings)
def get_all_times(message_channels, timezone=(-8)):
    print("Loading messages...")
    hours = []
    all_dates = []
    message_count = 0
    for channel in message_channels:
        messages = parse_csv(channel + "/messages.csv")
        for i in range(1,len(messages)):
            hours.append(((int(messages[i][1][11:13]))+timezone)%24)
            d = messages[i][1][:10]
            date = datetime.datetime.strptime(d, '%Y-%m-%d')
            all_dates.append(date)
            message_count += 1
    print("Loaded {} messages.".format(message_count))
    return hours, all_dates

# filters users/channels such that only those with message count above given threshold are considered
def filter_many(threshold, ids, message_dates):
    new_ids = []
    new_dates = []
    for i in range(len(ids)):
        if len(message_dates[i]) >= threshold:
            new_ids.append(ids[i])
            new_dates.append(message_dates[i])
    print("Number of channels considered: " + str(len(new_ids)))
    return new_ids, new_dates

# reformats 2D message date array into two 2D arrays:
# dates, sorted consecutive dates starting at the earliest message to the latest message
# counts, cumulative message counts with each user at each date
def reformat(message_dates):
    dates = []
    counts = []
    for i in range(len(message_dates)):
        dates.append([])
        counts.append([])
        min = message_dates[i][0]
        max = message_dates[i][0]
        for d in message_dates[i]:
            if min > d:
                min = d
            elif max < d:
                max = d
        for j in range(int((max-min).days)+1):
            date = min + datetime.timedelta(days=j)
            dates[i].append(date)
            counts[i].append(0)
        for d in message_dates[i]:
            for j in range(int((d-min).days),len(counts[i])):
                counts[i][j] += 1
    return dates, counts

# given a dictionary of known id and real name correspondences, replaces ids with names for easier visualization
def replace_ids_with_names(ids, names):
    for i in range(len(ids)):
        for id in names.keys():
            if ids[i] == id:
                ids[i] = names[id]
                break

# graphs the cumulative message counts with all users
# this is probably the most interesting one
def plot_messages_by_channel():
    message_channels = get_message_channels()
    ids, message_dates = get_dates_by_id(message_channels)
    ids, message_dates = filter_many(THRESHOLD, ids, message_dates)
    dates, counts = reformat(message_dates)
    replace_ids_with_names(ids, NAMES)
    for i in range(len(ids)):
        # if not ids[i] == "zach":
        #     continue
        plt.plot_date(dates[i], counts[i], linestyle="solid", marker=",", label=ids[i], color=COLORS[i%len(COLORS)])
    plt.legend()
    plt.xlabel("Date")
    plt.ylabel("Total messages")
    plt.show()

# graphs total messages sent over time
def plot_all_messages():
    message_channels = get_message_channels()
    hours, all_dates = get_all_times(message_channels, timezone=TIMEZONE)
    all_dates.sort()
    all_dates_new = []
    all_counts_new = []
    for i in range(int((all_dates[-1]-all_dates[0]).days)+1):
        all_dates_new.append((all_dates[0] + datetime.timedelta(days=i)))
        all_counts_new.append(0)
    for d in all_dates:
        for j in range(int((d-all_dates_new[0]).days),len(all_counts_new)):
            all_counts_new[j] += 1
    plt.plot_date(all_dates_new, all_counts_new, linestyle="solid", marker=",")
    plt.xlabel("Date")
    plt.ylabel("Total messages")
    plt.show()

# graphs distribution of messages sent each hour of the day
def plot_hours():
    message_channels = get_message_channels()
    hours, dates = get_all_times(message_channels, timezone=TIMEZONE)
    plt.hist(hours, bins=24)
    plt.xlabel("Hour of day")
    plt.ylabel("Total messages")
    plt.show()



# RUN CODE HERE !!!

# uncomment one of the lines to generate the desired figure :)
# names should be self-explanatory, the first one is the interesting one you're probably looking for

plot_messages_by_channel()
# plot_hours()
# plot_all_messages()
