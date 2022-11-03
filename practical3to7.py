from datetime import datetime


def timeToInt(value, index = -1):
  date_object = datetime.strptime(value, '%Y-%m-%d')
  result = int(date_object.strftime("%Y%m%d%H%M%S"))
  return result

Dataset = {
  "listA": [{
    "name": "John",
    "age": 20,
    "dateJoined": "2020-01-01",
  }, {
    "name": "John",
    "age": 25,
    "dateJoined": "2020-01-01",
  }, {
    "name": "John",
    "age": 30,
    "dateJoined": "2020-01-01",
  }, {
    "name": "Alice",
    "age": 35,
    "dateJoined": "2020-01-01",
  }, {
    "name": "Joe",
    "age": 40,
    "dateJoined": "2020-09-25",
  }],
  "listB": [{
    "name": "Kate",
    "age": 20,
    "dateJoined": "2020-01-01",
  }, {
    "name": "Lisa",
    "age": 21,
    "dateJoined": "2019-12-23",
  }, {
    "name": "mike",
    "age": 30,
    "dateJoined": "2020-04-26",
  }, {
    "name": "nancy",
    "age": 35,
    "dateJoined": "2020-08-20",
  }, {
    "name": "peter",
    "age": 40,
    "dateJoined": "2020-03-25",
  }
]
}


def quickSort2(arr, left, right, parameter):
    def partition2(arr, left, right, pivot):
        while left <= right:
            while arr[left][parameter] < pivot[parameter]:
                left +=1
            while arr[right][parameter] > pivot[parameter]:
                right -=1
            if left <= right:
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
                left += 1
                right -=1
        return left
    if left >= right:
        return 
    pivot = arr[int((left + right)/2)]
    index = partition2(arr, left, right, pivot)
    quickSort2(arr, left, index - 1, parameter)
    quickSort2(arr, index, right, parameter)

def quickSort(arr, left, right):
    def partition(arr, left, right, pivot):
        while left <= right:
            while timeToInt(arr[left]["dateJoined"]) < timeToInt(pivot["dateJoined"]):
                left +=1
            while timeToInt(arr[right]["dateJoined"]) > timeToInt(pivot["dateJoined"]):
                right -=1
            if left <= right:
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
                left += 1
                right -=1
        return left
    if left >= right:
        return 
    pivot = arr[int((left + right)/2)]
    index = partition(arr, left, right, pivot)
    quickSort(arr, left, index - 1)
    quickSort(arr, index, right)



def mergeSort(listA, listB):
    mergedList = listA + listB
    quickSort(arr=mergedList, left=0, right=len(mergedList) - 1)
    dates = []

    for i in mergedList:
        print(i)
        dates.append(i["dateJoined"])


    def getRepeatedValues(list):
        repeated_values = {}
        count = 1
        for i in range(len(list)):
            if i < count:
                continue
            index_dates= [i]
            index_names = [mergedList[i]["name"]]
            for j in range(i+1, len(list)):
                if list[i] == list[j]:
                    count +=1
                    index_dates.append(j)
                    index_names.append(mergedList[j]["name"])
                    repeated_values.update({list[i]: (index_dates, index_names)})
                    if j >= len(list) - 1:
                      return repeated_values
                else:
                    break

        print(repeated_values)
        return repeated_values
    
    repeated_dates = getRepeatedValues(dates).items()
    for key , value in repeated_dates:
      quickSort2(mergedList, value[0][0], value[0][len(value[0])-1], "name")
      names = [i for i in value[1]]
      repeated_names = getRepeatedValues(names).items()
      for key2, value2 in repeated_names:
        quickSort2(mergedList, value2[0][0], value2[0][len(value2[0])-1], "age")


    print("\n\n")
    for i in mergedList:
        print(i)

mergeSort(Dataset["listA"], Dataset["listB"])
