import json
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.json.base import create_json_agent
from langchain_community.tools.json.tool import JsonSpec, JSONToolkit

json_file_path = "./college_stats/stats.json"  # Ensure the file is in the correct directory
with open(json_file_path, "r") as f:
    json_data = json.load(f)

json_spec = JsonSpec(dict_=json_data, max_value_length=4000)
toolkit = JSONToolkit(json_spec=json_spec)

llm = ChatOpenAI(model_name="gpt-4", temperature=0)

agent_executor = create_json_agent(llm=llm, json_spec=json_spec, toolkit=toolkit, verbose=True)

query = "What is the next NCAA Men's Basketball game?"
response = agent_executor.run(query)

print(response)
