line_list = [
    "ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file, resetting to empty.",
    "ERROR 2014-07-03T23:24:31 supybot Exact error: IOError: [Errno 2] No such file or directory: 'conf/users.conf'",
    "ERROR 2014-07-03T23:24:31 supybot Invalid channel database, resetting to empty.",
    "ERROR 2014-07-03T23:24:31 supybot Exact error: IOError: [Errno 2] No such file or directory: 'conf/channels.conf'",
    "WARNING 2014-07-03T23:24:31 supybot Couldn't open ignore database: [Errno 2] No such file or directory: 'conf/ignores.conf'",
    "INFO 2014-07-03T23:27:51 supybot Shutdown initiated.",
    "INFO 2014-07-03T23:27:51 supybot Killing Driver objects.",
    "INFO 2014-07-03T23:31:22 supybot Shutdown initiated.",
    "INFO 2014-07-03T23:31:22 supybot Killing Driver objects.",
    "INFO 2014-07-03T23:31:22 supybot Shutdown complete."
]

new_list = list(filter(lambda x: "Shutdown initiated" in x, line_list))
print(new_list)

