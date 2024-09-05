A command-line Python program that returns a best-match given a new JSON object.

# Data

The originally provided data contains two applications - CRM App and Inventory App. The file is stored in `apps/original-apps.json`

### Generate additional App JSON files

Use ChatGPT to generate additional App JSONs.

Prompts:
1. Generate 100 similar to the uploaded App JSONs
2. For application names examples use the use cases from this website - https://www.quickbase.com/solutions
3. Could you combine the provided input and the generated JSON. Increment AppID
4. Create similar to this JSON with missing, rearranged and new values

Response:

> In this modified JSON: \
\- I created a new application called "Sales Tracking App".\
\- Rearranged the order of fields. \
\- Added a new field "Lead Score" in the Leads table and "Competitors" in the Opportunities table.\
\- New tables like "Conversions" were added to introduce a fresh perspective while retaining the structure.

### Generate a new application JSON

Use ChatGPT to generate a new app JSON.

Prompts:
1. Hey, Chat-GPT! Generate a new app JSON with a similar structure, bit remove, rearrange and add new tables and fields. Use CRM App JSON.

Response:

> Here’s a modified version of your provided JSON structure for a CRM app, featuring rearranged and new tables and fields:\
\
Key Changes Made:\
\- Renamed "Companies" to "Clients" and adjusted related terms.\
\- Separated the "Lead Status" and "Lead Source" into more general terms.\
\- Added a new table for "Opportunities" with relevant fields.\
\- Removed some fields from previous tables while maintaining core functionality.\
\-The structure reflects a more streamlined CRM focus while retaining useful relationships and summaries.


# Similarity Metrics

Given a new application schema, the model calculates the **cosine distance** between all fields in the provided schema and all fields in each of the existing applications. The model selects as a *best-match* the application with the highest average cosine similarity.