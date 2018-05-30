import ijson
import io


# this function open a json file using ijson and pass each line
# to one txt. Thank you to Mr-IDE at StackOverflow.
def jsonToTxt(json_filename, goal_path):
    path = goal_path  # this will be the path where the code puts the txts
    dont_allow = ["reviewerID", "asin", "reviewerName", "helpful", "reviewText", "overall", "summary", "reviewTime",
                  "unixReviewTime"]
    with open(json_filename, encoding="UTF-8") as json_file:
        count = 0  # counts the txt generated
        bandera=False
        for line_number, line in enumerate(json_file):
            if count >= 10481487:
                line_as_file = io.StringIO(line)
                # Use a new parser for each line
                json_parser = ijson.parse(line_as_file)
                filebody = " "
                for prefix, type, value in json_parser:  # each item from the line, only we need the value
                    if value is None:
                        pass
                    else:
                        if value not in dont_allow:  # don't allow trash
                            filebody += str(value)  # txt body
                            filebody += " "
                path += str(count)
                path += ".txt"
                file = open(path, "w")
                file.write(filebody)
                file.close()
                path = goal_path
            else:
                count += 1
                break
    json_file.close()
