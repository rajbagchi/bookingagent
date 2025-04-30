### 🏗️ Architecture Diagram


          ┌──────────────────────────────┐
          │        User (chat)           │
          └──────────────┬───────────────┘
                         │  free-text
                         ▼
          ┌──────────────────────────────┐
          │  UserIntentAgent (GPT-4o)    │
          └──────────────┬───────────────┘
                         │  topic_key
                         ▼
          ┌──────────────────────────────┐
          │   BookingAgent (LangChain)   │
          └──────────────┬───────────────┘
                         │  booking URL
                         ▼
          ┌──────────────────────────────┐
          │   Microsoft Bookings page    │
          └──────────────────────────────┘


1. **UserIntentAgent** classifies free-text into one of 20 `topic_key` strings.  
2. It sends a `link_request` message to **BookingAgent**.  
3. **BookingAgent** calls the LangChain tool `get_booking_link(topic_key)`.  
4. The static public booking URL is sent back to the user.


### 🚀 Quick Start

```bash
# 1. Clone & enter project
git clone <repo> && cd mcp_langchain_bot

# 2. Python environment
python -m venv .venv && source .venv/bin/activate   # Windows: .\.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set Azure OpenAI variables
export AZURE_OPENAI_API_KEY=... \
       AZURE_OPENAI_ENDPOINT=...

# 5. Run CLI demo

python run_simulation.py

A booking link will be printed for the simulated user.


### 💬 Example Interaction (CLI)

User : I need structural engineering help.
Bot  : https://outlook.office365.com/.../StructuralEngineering

User : Questions about tree code on my lot.
Bot  : https://outlook.office365.com/.../ZoningTreeCode


###🗄️ Folder Layout

requirements.txt        # Python deps
README.md               # This file
│
├─ mcp_server/
│   core.py             # Message & Agent base classes
│   runtime.py          # Simple message-queue loop
│
├─ agents/
│   user_intent_agent.py  # GPT-4o classifier agent
│   booking_agent.py      # Returns booking links
│
├─ tools/
│   ms_booking_tool.py    # get_booking_link() LangChain tool
│
├─ langchain_env.py       # AzureChatOpenAI config
├─ appointment_flows.py   # (stub for future dialog logic)
└─ run_simulation.py      # CLI driver




### 🔑 Appointment Keys & Slugs (excerpt)

| Key                            | Booking slug                |
|--------------------------------|-----------------------------|
| `land_use`                     | `LandUseAppointment`        |
| `environmental`                | `EnvironmentalAppointment`  |
| `zoning_tree`                  | `ZoningTreeCode`            |
| `residential_building`         | `ResidentialBuildingCode`   |
| `commercial_building`          | `CommercialBuildingCode`    |
| `structural_engineering`       | `StructuralEngineering`     |
| … etc. (see `ms_booking_tool.py` for full list) |


### 🛠️ Extending

Replace static tool with Graph-API scheduling.

Add DialogManagerAgent to collect address, email, etc.

Connect a web UI , an open source chatbot or MS Teams bot to the runtime.


### 📄 License
MIT
