from study_ai.tools import (
    weather_tool,
    calculator_tool,
    search_tool,
)


def main():
   print("============== Weather Tool ==================")
   weather = weather_tool.invoke(
       {
           "city":"Kathmandu",
       }
   )
   print(weather)
   print()
   print("=========== Calucator Tool ==========")
   result =calculator_tool.invoke(
       {
           "number1": 20,
           "number2": 4,
           "operation": "divide",
       }
   )
   print(result)
   print()
   print("======== Search Tool ========")
   search = search_tool.invoke(
       {
           "query":"LangChain",
       }
   )
   print(search)
if __name__ == "__main__":
    main()
