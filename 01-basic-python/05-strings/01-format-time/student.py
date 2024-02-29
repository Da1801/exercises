# Write your code here
def format_time(hours, minutes, seconds):
    def format(k):
        return str(k).rjust(2,"0")
    new_hours = format(hours)
    new_minutes = format(minutes)
    new_seconds = format(seconds)
    return f"{new_hours}:{new_minutes}:{new_seconds}"
