import csv
import time
from graph import graph 
total=0
correct=0
total_latency=0
with open("test_question.csv",mode="r",encoding="utf=8")as file:
    reader=csv.DictReader(file)
    for row in reader:
        question= row["question"]
        expected=row["expected_agent"]
        start=time.time()
        result=graph.invoke({
            "question":question
        })

        latency= time.time()-start
        predicted=result["route"]
        is_correct= predicted==expected

        if is_correct:
            correct+=1
            total+=1
            total_latency+=latency
            print("Question :", question)
            print("Expected :", expected)
            print("Predicted:", predicted)
            print("Correct  :", is_correct)
            print("Latency  :", round(latency, 2), "sec")
            print("Sources  :", len(result["sources"]))
            print()
accuracy = (correct / total) * 100
average_latency = total_latency / total
print(f"Total Questions   : {total}")
print(f"Correct Routes    : {correct}")
print(f"Routing Accuracy  : {accuracy:.2f}%")
print(f"Average Latency   : {average_latency:.2f} sec")