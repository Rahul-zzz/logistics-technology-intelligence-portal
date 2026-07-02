import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Logistics Technology Intelligence Portal",
    page_icon="🚚",
    layout="wide"
)

# ==================================================
# LOAD DATA
# ==================================================

companies = pd.read_excel("companies.xlsx")
systems = pd.read_excel("systems.xlsx")
mapping = pd.read_excel("company_system_mapping.xlsx")
mapping_dict = {
    "Low": 30,
    "Medium": 60,
    "High": 90
}

companies["Technology Maturity"] = companies["Technology Maturity"].replace(mapping_dict)
companies["AI Readiness"] = companies["AI Readiness"].replace(mapping_dict)

companies["Technology Maturity"] = pd.to_numeric(companies["Technology Maturity"], errors="coerce")
companies["AI Readiness"] = pd.to_numeric(companies["AI Readiness"], errors="coerce")

# ==================================================
# TITLE
# ==================================================

st.title("🚚 Logistics Technology Intelligence Portal")

st.markdown("""
Analyze logistics companies, technologies, ERP systems,
transportation platforms, AI readiness and operational maturity.
""")

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Choose Section",
    [
        "🏢 Company Explorer",
        "🚚 Last Mile Delivery",
        "⚙️ System Explorer",
        "📊 Technology Dashboard",
        "🤖 AI Readiness",
        "⚖️ Company Comparison",
        "📈 Insights & Recommendations"
    ]
)

# ==================================================
# COMPANY EXPLORER
# ==================================================

if page == "🏢 Company Explorer":

    st.header("🏢 Company Explorer")

    company = st.selectbox(
        "Select Company",
        companies["Company Name"]
    )

    selected_company = companies[
        companies["Company Name"] == company
    ].iloc[0]
    st.image(selected_company["Logo Url"], width=120)

    # ----------------------------------------------
    # COMPANY OVERVIEW
    # ----------------------------------------------

    st.subheader("📌 Company Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Industry",
            selected_company["Industry"]
        )

    with col2:
        st.metric(
            "Headquarters",
            selected_company["Headquarters"]
        )

    with col3:
        st.metric(
            "Company Size",
            selected_company["Company Size"]
        )

    # ----------------------------------------------
    # COMPANY INFORMATION
    # ----------------------------------------------

    st.subheader("🏢 Company Information")

    st.write("Founded:", selected_company["Founded"])
    st.write("Services:", selected_company["Services"])
    st.write("Technology Focus:", selected_company["Technology Focus"])

    # ----------------------------------------------
    # CUSTOMERS
    # ----------------------------------------------

    st.subheader("👥 Top Customers")

    st.info(
        selected_company["Top Customers"]
    )

    # ----------------------------------------------
    # TECHNOLOGY STACK
    # ----------------------------------------------

    st.subheader("⚙️ Technology Stack")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success(
            f"ERP: {selected_company['ERP System']}"
        )

    with col2:
        st.success(
            f"TMS: {selected_company['TMS System']}"
        )

    with col3:
        st.success(
            f"Fleet: {selected_company['Fleet System']}"
        )

    # ----------------------------------------------
    # DATA GENERATED
    # ----------------------------------------------

    st.subheader("📊 Data Generated")

    st.write(
        selected_company["Data Generated"]
    )

    # ----------------------------------------------
    # WORKER TOUCHPOINTS
    # ----------------------------------------------

    st.subheader("👷 Worker Touchpoints")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            selected_company["Driver Touchpoint"]
        )

    with col2:
        st.info(
            selected_company["Warehouse Touchpoint"]
        )

    with col3:
        st.info(
            selected_company["Manager Touchpoint"]
        )

    # ----------------------------------------------
    # CHALLENGES
    # ----------------------------------------------

    st.subheader("⚠️ Current Challenges")

    st.error(
        selected_company["Current Challenges"]
    )

    # ----------------------------------------------
    # FUTURE OPPORTUNITIES
    # ----------------------------------------------

    st.subheader("🚀 Future Opportunities")

    st.success(
        selected_company["Future Opportunities"]
    )

    # ----------------------------------------------
    # COMPETITORS
    # ----------------------------------------------

    st.subheader("🏁 Key Competitors")

    st.warning(
        selected_company["Key Competitors"]
    )

    # ----------------------------------------------
    # TECHNOLOGY ASSESSMENT
    # ----------------------------------------------

    st.subheader("📈 Technology Assessment")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Technology Maturity",
            selected_company["Technology Maturity"]
        )

    with col2:
        st.metric(
            "AI Readiness",
            selected_company["AI Readiness"]
        )

    # ==============================================
    # ASSOCIATED SYSTEMS
    # ==============================================

    st.markdown("---")

    st.header("🔗 Associated Systems")

    company_systems = mapping[
        mapping["Company Name"] == company
    ]

    for _, row in company_systems.iterrows():

        system_name = row["System Name"]

        matching_system = systems[
            systems["System Name"] == system_name
        ]

        if len(matching_system) == 0:
            continue

        system_data = matching_system.iloc[0]

        with st.expander(system_name):

            if "Vendor" in systems.columns:
                st.write("Vendor:", system_data["Vendor"])

            if "Category" in systems.columns:
                st.write("Category:", system_data["Category"])

            if "What It Does" in systems.columns:
                st.write("What It Does:", system_data["What It Does"])

            if "Pricing Model" in systems.columns:
                st.write("Pricing Model:", system_data["Pricing Model"])

            if "Key Features" in systems.columns:
                st.subheader("Features")
                st.info(system_data["Key Features"])

            if "Worker Touchpoint" in systems.columns:
                st.subheader("Worker Interaction")
                st.write(
                    "Touchpoint:",
                    system_data["Worker Touchpoint"]
                )

            if "Mobile App" in systems.columns:
                st.write(
                    "Mobile App:",
                    system_data["Mobile App"]
                )

            if "Local Language Support" in systems.columns:
                st.write(
                    "Language Support:",
                    system_data["Local Language Support"]
                )

            if "Advantages" in systems.columns:
                st.subheader("Advantages")
                st.success(system_data["Advantages"])

            if "Limitations" in systems.columns:
                st.subheader("Limitations")
                st.error(system_data["Limitations"])

            if "Future Potential" in systems.columns:
                st.subheader("Future Potential")
                st.warning(system_data["Future Potential"])
# ==============================
# 📌 Data Source Information
# ==============================

    import pandas as pd
    import streamlit as st

    st.markdown("---")
    st.subheader("📌 Data Source Information")

    # Read the Company Explorer data source Excel file
    df = pd.read_excel("Data_Source.xlsx")

    # Display only Company and Data Type columns
    display_df = df[["Company", "Data Type"]]

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )
# ==================================================
# SYSTEM EXPLORER
# ==================================================

elif page == "⚙️ System Explorer":

    st.header("⚙️ System Explorer")

    # ----------------------------------------------
    # SELECT SYSTEM
    # ----------------------------------------------

    system_name = st.selectbox(
        "Select System",
        systems["System Name"]
    )

    selected_system = systems[
        systems["System Name"] == system_name
    ].iloc[0]

    # ----------------------------------------------
    # SYSTEM OVERVIEW
    # ----------------------------------------------

    st.subheader("📌 System Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        if "Vendor" in systems.columns:
            st.metric(
                "Vendor",
                selected_system["Vendor"]
            )

    with col2:
        if "Category" in systems.columns:
            st.metric(
                "Category",
                selected_system["Category"]
            )

    with col3:
        if "Pricing Model" in systems.columns:
            st.metric(
                "Pricing",
                selected_system["Pricing Model"]
            )

    # ----------------------------------------------
    # WHAT IT DOES
    # ----------------------------------------------

    if "What It Does" in systems.columns:

        st.subheader("📖 What It Does")

        st.write(
            selected_system["What It Does"]
        )

    # ----------------------------------------------
    # FEATURES
    # ----------------------------------------------

    if "Key Features" in systems.columns:

        st.subheader("🚀 Key Features")

        st.info(
            selected_system["Key Features"]
        )

    # ----------------------------------------------
    # WORKER INTERACTION
    # ----------------------------------------------

    st.subheader("👷 Worker Interaction")

    if "Worker Touchpoint" in systems.columns:

        st.write(
            "Touchpoint:",
            selected_system["Worker Touchpoint"]
        )

    if "Mobile App" in systems.columns:

        st.write(
            "Mobile App:",
            selected_system["Mobile App"]
        )

    if "Local Language Support" in systems.columns:

        st.write(
            "Language Support:",
            selected_system["Local Language Support"]
        )

    # ----------------------------------------------
    # ADVANTAGES
    # ----------------------------------------------

    if "Advantages" in systems.columns:

        st.subheader("✅ Advantages")

        st.success(
            selected_system["Advantages"]
        )

    # ----------------------------------------------
    # LIMITATIONS
    # ----------------------------------------------

    if "Limitations" in systems.columns:

        st.subheader("⚠️ Limitations")

        st.error(
            selected_system["Limitations"]
        )

    # ----------------------------------------------
    # FUTURE POTENTIAL
    # ----------------------------------------------

    if "Future Potential" in systems.columns:

        st.subheader("🔮 Future Potential")

        st.warning(
            selected_system["Future Potential"]
        )

    # ----------------------------------------------
    # COMPANIES USING THIS SYSTEM
    # ----------------------------------------------

    st.markdown("---")

    st.subheader("🏢 Companies Using This System")

    system_companies = mapping[
        mapping["System Name"] == system_name
    ]

    if len(system_companies) > 0:

        for _, row in system_companies.iterrows():

            st.success(
                row["Company Name"]
            )

    else:

        st.info(
            "No companies mapped to this system."
        )
# ==============================
# 📌 Data Source Information
# ==============================

    import pandas as pd
    import streamlit as st

    st.markdown("---")
    st.subheader("📌 Data Source Information")

    # Read the System Explorer data source Excel file
    df = pd.read_excel("Data_Source.xlsx")

    # Read only the 'System Explorer' sheet
    display_df = pd.read_excel(
        "Data_Source.xlsx",
        sheet_name="System Explorer"
    )


    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )
# ==================================================
# TECHNOLOGY DASHBOARD
# ==================================================

elif page == "📊 Technology Dashboard":

    st.header("📊 Technology Dashboard")
   
    # ==========================================
    # KPI SECTION
    # ==========================================

    total_companies = len(companies)

    total_systems = len(systems)

    enterprise_companies = len(
        companies[
            companies["Company Size"] == "Enterprise"
        ]
    )

    try:
        avg_ai = pd.to_numeric(
            companies["AI Readiness"],
            errors="coerce"
        ).mean()
    except:
        avg_ai = 0

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Companies",
            total_companies
        )

    with col2:
        st.metric(
            "Total Systems",
            total_systems
        )

    with col3:
        st.metric(
            "Enterprise Companies",
            enterprise_companies
        )

    with col4:
        st.metric(
            "Average AI Readiness",
            round(avg_ai, 1)
        )

    st.markdown("---")

    # ==========================================
    # TECHNOLOGY MATURITY
    # ==========================================

    if "Technology Maturity" in companies.columns:

        st.subheader("📈 Technology Maturity by Company")

        maturity_chart = px.bar(
            companies,
            x="Company Name",
            y="Technology Maturity",
            title="Technology Maturity"
        )

        st.plotly_chart(
            maturity_chart,
            use_container_width=True
        )

    # ==========================================
    # AI READINESS
    # ==========================================

    if "AI Readiness" in companies.columns:

        st.subheader("🤖 AI Readiness by Company")

        ai_chart = px.bar(
            companies,
            x="Company Name",
            y="AI Readiness",
            title="AI Readiness"
        )

        st.plotly_chart(
            ai_chart,
            use_container_width=True
        )
    # ==========================================
    # MOST USED SYSTEMS
    # ==========================================

    st.subheader("⚙️ Most Used Systems")

    system_count = (
        mapping["System Name"]
        .value_counts()
        .reset_index()
    )

    system_count.columns = [
        "System Name",
        "Count"
    ]

    usage_chart = px.bar(
        system_count,
        x="System Name",
        y="Count",
        title="System Usage Across Companies"
    )

    st.plotly_chart(
        usage_chart,
        use_container_width=True
    )

    # ==========================================
    # SYSTEM CATEGORY DISTRIBUTION
    # ==========================================

    if "Category" in systems.columns:

        st.subheader("📊 System Category Distribution")

        category_chart = px.pie(
            systems,
            names="Category",
            title="System Categories"
        )

        st.plotly_chart(
            category_chart,
            use_container_width=True
        )
        st.markdown("---")

        st.subheader("📖 Technology & AI Score Guide")

        st.info("""
🔴 0 - 30  → Low Technology Maturity / AI Readiness

🟡 31 - 60 → Medium Technology Maturity / AI Readiness

🟢 61 - 90 → High Technology Maturity / AI Readiness

🚀 91 - 100 → Industry Leader
""")
# ==============================
# 📌 Data Source Information
# ==============================

    import pandas as pd
    import streamlit as st

    st.markdown("---")
    st.subheader("📌 Data Source Information")

    # Read the Technology Dashboard sheet
    df = pd.read_excel(
        "Data_Source.xlsx",      # Change this to your actual Excel file path
        sheet_name="Technology dashboard"
    )

    # Display only the required columns
    display_df = df[["Dashboard Component", "Data Type"]]

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )
# ==================================================
# AI READINESS DASHBOARD
# ==================================================

elif page == "🤖 AI Readiness":

    st.header("🤖 AI Readiness Dashboard")

    # ----------------------------------------------
    # KPI CARDS
    # ----------------------------------------------

    ai_scores = pd.to_numeric(
        companies["AI Readiness"],
        errors="coerce"
    )

    avg_ai = ai_scores.mean()
    max_ai = ai_scores.max()
    min_ai = ai_scores.min()

    ai_leaders = len(
        companies[
            ai_scores >= 80
        ]
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Average AI Score",
            round(avg_ai, 1)
        )

    with col2:
        st.metric(
            "Highest Score",
            max_ai
        )

    with col3:
        st.metric(
            "Lowest Score",
            min_ai
        )

    with col4:
        st.metric(
            "AI Leaders",
            ai_leaders
        )

    st.markdown("---")

    # ----------------------------------------------
    # AI READINESS RANKING
    # ----------------------------------------------

    st.subheader("🏆 AI Readiness Ranking")

    ai_rank = companies.copy()

    ai_rank["AI Readiness"] = pd.to_numeric(
        ai_rank["AI Readiness"],
        errors="coerce"
    )

    ai_rank = ai_rank.sort_values(
        "AI Readiness",
        ascending=False
    )

    ai_chart = px.bar(
        ai_rank,
        x="Company Name",
        y="AI Readiness",
        title="AI Readiness Ranking"
    )

    st.plotly_chart(
        ai_chart,
        use_container_width=True
    )

    # ----------------------------------------------
    # AI LEADERS
    # ----------------------------------------------

    st.subheader("🚀 AI Leaders")

    leaders = ai_rank[
        ai_rank["AI Readiness"] >= 80
    ]

    if len(leaders) > 0:

        columns_to_show = [
            col for col in [
                "Company Name",
                "AI Readiness",
                "Technology Maturity"
            ]
            if col in leaders.columns
        ]

        st.dataframe(
            leaders[columns_to_show]
        )

    else:
        st.info("No AI leaders found.")

    # ----------------------------------------------
    # AI IMPROVEMENT TARGETS
    # ----------------------------------------------

    st.subheader("⚠️ AI Improvement Targets")

    laggards = ai_rank[
        ai_rank["AI Readiness"] < 60
    ]

    if len(laggards) > 0:

        columns_to_show = [
            col for col in [
                "Company Name",
                "AI Readiness",
                "Technology Maturity"
            ]
            if col in laggards.columns
        ]

        st.dataframe(
            laggards[columns_to_show]
        )

    else:
        st.success(
            "No companies below AI threshold."
        )

    # ----------------------------------------------
    # AI OPPORTUNITY ANALYSIS
    # ----------------------------------------------

    st.subheader("💡 AI Opportunity Areas")

    opportunity_data = pd.DataFrame({
        "Area": [
            "Route Optimization",
            "Demand Forecasting",
            "Warehouse Automation",
            "Predictive Maintenance",
            "Customer Support AI"
        ],
        "Impact": [
            95,
            90,
            85,
            80,
            75
        ]
    })

    opportunity_chart = px.bar(
        opportunity_data,
        x="Area",
        y="Impact",
        title="AI Opportunity Areas"
    )

    st.plotly_chart(
        opportunity_chart,
        use_container_width=True
    )

    # ----------------------------------------------
    # RECOMMENDATIONS
    # ----------------------------------------------

    st.subheader("📋 AI Recommendations")

    st.success("""
• Prioritize Route Optimization AI

• Improve Warehouse Automation

• Expand Predictive Analytics

• Implement AI-based Customer Support

• Integrate AI with ERP and TMS systems
""")
# ==============================
# 📌 Data Source Information
# ==============================

    import pandas as pd
    import streamlit as st

    st.markdown("---")
    st.subheader("📌 Data Source Information")

    # Read the AI Readiness sheet
    df = pd.read_excel(
        "Data_Source.xlsx",      # Replace with your actual Excel file path
        sheet_name="AI Readiness"
    )

    # Display only the required columns
    display_df = df[["Dashboard Component", "Data Type"]]

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

# ==================================================
# LAST MILE DELIVERY
# ==================================================

elif page == "🚚 Last Mile Delivery":

    st.header("🚚 Last Mile Delivery Intelligence Center")

    st.markdown("""
Welcome to the **Last Mile Delivery Intelligence Center**.

This dashboard provides a comprehensive overview of:

- Last Mile Delivery Fundamentals
- Market Size & Growth
- Industry Insights
- Delivery Ecosystem
- Technologies Used
- AI Applications
- Major Logistics Companies
- Future Trends
- Business Recommendations
""")

    # ==================================================
    # WHAT IS LAST MILE DELIVERY
    # ==================================================

    st.markdown("---")

    st.subheader("📖 What is Last Mile Delivery?")

    st.info("""
Last Mile Delivery is the final stage of the logistics supply chain where a shipment moves from the local distribution center or delivery hub to the customer's doorstep.

Although it is the shortest transportation distance, it is the most expensive and operationally complex part of logistics.

Major Objectives

• Fast Delivery

• Accurate Delivery

• Low Delivery Cost

• Better Customer Experience

• Real-time Tracking

• Digital Proof of Delivery
""")
# ==================================================
# MARKET OVERVIEW
# ==================================================

    st.markdown("---")

    st.subheader("📊 Market Overview")

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric(
            "Global Market",
            "$181.6 Billion"
        )

    with kpi2:
        st.metric(
            "India CAGR",
            "14.4%"
        )

    with kpi3:
        st.metric(
            "Delivery Success",
            "95%"
        )

    with kpi4:
        st.metric(
            "Last Mile Cost",
            "53%"
        )

    st.info("""
    Nearly 53% of total logistics costs occur during the last mile because every package must reach an individual customer location.
    """)
# ==================================================
# MARKET GROWTH
# ==================================================

    st.markdown("---")

    st.subheader("📈 Global Market Growth")

    growth_df = pd.DataFrame({

        "Year":[
            2022,
            2023,
            2024,
            2025,
            2026,
            2027,
            2028
        ],

        "Market Size":[
            120,
            136,
            150,
            166,
            182,
            201,
            221
        ]

    })

    growth_chart = px.line(

        growth_df,

        x="Year",

        y="Market Size",

        markers=True,

        title="Global Last Mile Delivery Market"

    )

    st.plotly_chart(
        growth_chart,
        use_container_width=True
    )
# ==================================================
# MARKET SEGMENTATION
# ==================================================

    st.markdown("---")

    st.subheader("🌍 Last Mile Delivery Market Segmentation")

    segment_df = pd.DataFrame({
        "Segment": [
            "E-Commerce",
            "Retail",
            "Food Delivery",
            "Healthcare",
            "Courier & Parcel",
            "Grocery Delivery"
        ],
        "Market Share (%)": [
            40,
            18,
            16,
            10,
            9,
            7
        ]
    })

    segment_chart = px.pie(
        segment_df,
        names="Segment",
        values="Market Share (%)",
        hole=0.45,
        title="Global Last Mile Delivery Market Share"
    )

    st.plotly_chart(
        segment_chart,
        use_container_width=True
    )
# ==================================================
# DIGITAL TRANSFORMATION
# ==================================================

    st.markdown("---")

    st.subheader("💻 Digital Transformation in Last Mile Logistics")

    digital_df = pd.DataFrame({

        "Technology": [

            "Artificial Intelligence",

            "IoT",

            "GPS Tracking",

            "Cloud Computing",

            "Mobile Applications",

            "Warehouse Automation",

            "Electric Vehicles",

            "Digital Payments"

        ],

        "Adoption (%)": [

            88,

            76,

            95,

            84,

            97,

            72,

            61,

            99

        ]

    })

    digital_chart = px.bar(

        digital_df,

        x="Technology",

        y="Adoption (%)",

        color="Adoption (%)",

        title="Technology Adoption Across Logistics Industry"

    )

    st.plotly_chart(
        digital_chart,
        use_container_width=True
    )

    # ==================================================
    # INDUSTRY MATURITY SCORECARD
    # ==================================================

    st.markdown("---")

    st.subheader("⭐ Industry Maturity Scorecard")

    st.caption(
        "Evaluate the current maturity of the logistics industry across key technology and operational capabilities."
    )

    left_col, right_col = st.columns(2)

    with left_col:

        st.metric(label="Technology Adoption", value="95/100")
        st.progress(95)

        st.metric(label="Digital Transformation", value="90/100")
        st.progress(90)

        st.metric(label="AI Adoption", value="87/100")
        st.progress(87)

        st.metric(label="Customer Experience", value="91/100")
        st.progress(91)

    with right_col:

        st.metric(label="Automation", value="84/100")
        st.progress(84)

        st.metric(label="Operational Visibility", value="89/100")
        st.progress(89)

        st.metric(label="Sustainability", value="81/100")
        st.progress(81)

        st.metric(label="Innovation", value="86/100")
        st.progress(86)

    st.info("""
### 📌 Score Guide

🟢 **90–100** : Excellent

🟡 **70–89** : Good

🟠 **50–69** : Moderate

🔴 **Below 50** : Needs Improvement
""")

    st.success("""
### 💡 Business Insight

The logistics industry demonstrates strong maturity in digital transformation,
technology adoption, customer experience, and automation. Continued investment
in AI, sustainability, and operational visibility will strengthen long-term
business performance and competitiveness.
""")
# ==================================================
# TECHNOLOGY COMPARISON DASHBOARD
# ==================================================

    st.markdown("---")
    st.header("📊 Technology Comparison Dashboard")

    comparison_df = pd.DataFrame({

        "Technology":[
            "ERP",
            "WMS",
            "TMS",
            "Fleet",
            "GPS",
            "AI",
            "IoT",
            "RFID",
            "Mobile App",
            "ePOD"
        ],

        "Business Impact":[95,90,92,88,89,97,84,82,91,90],

        "Implementation Cost":[
            "High",
            "Medium",
            "Medium",
            "Medium",
            "Low",
            "High",
            "Medium",
            "Low",
            "Medium",
            "Low"
        ],

        "Automation (%)":[
            90,
            88,
            91,
            85,
            89,
            96,
            82,
            80,
            90,
            87
        ]

    })

    st.dataframe(
        comparison_df,
        use_container_width=True
    )

    impact_chart = px.bar(
        comparison_df,
        x="Technology",
        y="Business Impact",
        color="Business Impact",
        title="Business Impact Score"
    )

    st.plotly_chart(
        impact_chart,
        use_container_width=True
    )
# ==================================================
    # TECHNOLOGY ADOPTION
    # ==================================================

    st.markdown("---")
    st.subheader("📈 Industry Technology Adoption")

    adoption_df = pd.DataFrame({

        "Technology":[
            "GPS",
            "ERP",
            "Mobile App",
            "TMS",
            "WMS",
            "AI",
            "IoT",
            "RFID",
            "ePOD"
        ],

        "Adoption (%)":[
            95,
            87,
            98,
            84,
            81,
            72,
            65,
            78,
            86
        ]

    })

    adoption_chart = px.bar(
        adoption_df,
        x="Technology",
        y="Adoption (%)",
        color="Adoption (%)",
        title="Technology Adoption Across Logistics Industry"
    )

    st.plotly_chart(
        adoption_chart,
        use_container_width=True
    )
# ==================================================
    # KEY STATISTICS
    # ==================================================

    st.markdown("---")

    st.subheader("📊 Key Industry Statistics")

    statistics_df = pd.DataFrame({

        "Metric":[

            "Average Delivery Time",

            "Delivery Success Rate",

            "Average Fuel Cost Share",

            "Customer Tracking Usage",

            "Digital Proof of Delivery",

            "AI Route Optimization Adoption"

        ],

        "Value":[

            "24 Hours",

            "95%",

            "35%",

            "92%",

            "89%",

            "78%"

        ]

    })

    st.dataframe(
        statistics_df,
        use_container_width=True
    )


    # ==================================================
    # DELIVERY FLOW
    # ==================================================

    st.markdown("---")

    st.subheader("🔄 Last Mile Delivery Workflow")

    st.code("""
Manufacturer
      │
      ▼
Warehouse
      │
      ▼
Distribution Center
      │
      ▼
Sorting Hub
      │
      ▼
Last Mile Hub
      │
      ▼
Delivery Executive
      │
      ▼
Customer
      │
      ▼
Digital Proof of Delivery
""")
# ==================================================
# INDUSTRY GROWTH DRIVERS
# ==================================================

    st.markdown("---")

    st.subheader("📈 Industry Growth Drivers")

    st.success("""
### Key Growth Drivers

**🛒 Rapid Growth of E-Commerce**
- Online shopping continues to increase parcel volumes, driving demand for efficient last-mile delivery services.

**⚡ Same-Day & Next-Day Delivery**
- Customers increasingly expect faster deliveries, encouraging companies to optimize delivery operations.

**📱 Mobile Commerce Expansion**
- Smartphones and digital payment platforms have accelerated online purchasing behavior.

**🏙️ Hyperlocal Delivery**
- Businesses are investing in local fulfillment centers to enable faster deliveries within cities.

**💳 Digital Payments**
- Cashless transactions simplify delivery operations and improve customer convenience.

**🌆 Urbanization**
- Growing urban populations increase demand for scalable logistics networks.

**🤖 AI-Powered Logistics**
- Artificial Intelligence improves route optimization, demand forecasting, fleet utilization, and operational efficiency.
""")

# ==================================================
# BUSINESS RISKS & OPERATIONAL CHALLENGES
# ==================================================

    st.markdown("---")

    st.subheader("⚠️ Business Risks & Operational Challenges")

    with st.expander("💰 High Delivery Cost"):

        st.write("""
The last mile is the most expensive stage of the logistics supply chain,
accounting for nearly **53% of total logistics costs**.

### Why does this happen?

• Every shipment is delivered individually to customers instead of in bulk.

• Traffic congestion increases travel time and fuel consumption.

• Failed delivery attempts require additional transportation.

• Rising fuel prices increase operational expenses.

• Driver wages and vehicle maintenance significantly contribute to delivery costs.

### Business Impact

✅ Reduced Profit Margins

✅ Higher Cost per Shipment

✅ Lower Fleet Productivity

✅ Increased Operational Expenses
""")

    with st.expander("🔄 Reverse Logistics"):

        st.write("""
Reverse logistics refers to transporting products from customers back to warehouses
or sellers due to returns, exchanges, damaged products, or incorrect deliveries.

### Common Reasons

• Product Returns

• Wrong Deliveries

• Damaged Goods

• Product Exchange

• Warranty Claims

### Why is it challenging?

• Additional transportation is required.

• Returned products must be inspected and restocked.

• Warehouses require additional labor and storage.

• Return processing increases operational complexity.

### Business Impact

✅ Increased Logistics Cost

✅ Inventory Management Complexity

✅ Additional Warehouse Workload

✅ Reduced Profitability
""")

    st.info("""
### Other Industry Challenges

• Traffic Congestion

• Failed Deliveries

• Fuel Price Fluctuation

• Driver Shortage

• Rising Customer Expectations
""")

# ==================================================
# BUSINESS INSIGHT
# ==================================================

    st.markdown("---")

    st.subheader("💡 Business Insight")

    st.success("""
Although last-mile delivery represents the shortest segment of the logistics
journey, it contributes the highest operational cost. Organizations that
adopt AI-powered route optimization, GPS-based fleet tracking, warehouse
automation, and efficient return management can significantly reduce costs,
improve delivery performance, and enhance customer satisfaction.

**Key Takeaway**

• Optimize delivery routes using AI.

• Improve fleet visibility with GPS tracking.

• Automate warehouse and return operations.

• Reduce failed deliveries through real-time customer communication.

• Invest in digital technologies to improve profitability and operational efficiency.
""")
    # ==================================================
    # SUMMARY
    # ==================================================

    st.markdown("---")

    st.subheader("📌 Last Mile Delivery Summary")

    st.success("""
    ✔ Last Mile Delivery is the fastest growing logistics segment worldwide.

    ✔ Customer expectations are shifting towards Same-Day and Next-Day delivery.

    ✔ AI, GPS, IoT and Mobile Applications are transforming delivery operations.

    ✔ Technology adoption is reducing operational cost while improving customer satisfaction.

    ✔ Companies investing in automation are becoming industry leaders.

    ✔ Sustainable logistics and Electric Vehicles will define the future of Last Mile Delivery.
    """)
    # ==================================================
    # LAST MILE DELIVERY ECOSYSTEM
    # ==================================================

    st.markdown("---")

    st.header("🏭 Last Mile Delivery Ecosystem")

    st.write("""
The Last Mile Delivery ecosystem consists of multiple stakeholders, technologies,
vehicles, and operational centers working together to deliver products efficiently
to customers.
""")

    # --------------------------------------------------
    # END-TO-END FLOW
    # --------------------------------------------------

    st.subheader("🔄 Complete Delivery Flow")

    st.code("""
Manufacturer
      │
      ▼
Supplier
      │
      ▼
Warehouse
      │
      ▼
Fulfillment Center
      │
      ▼
Sorting Center
      │
      ▼
Regional Hub
      │
      ▼
Last Mile Hub
      │
      ▼
Delivery Executive
      │
      ▼
Customer
      │
      ▼
Digital Proof of Delivery
""")

    # --------------------------------------------------
    # STAKEHOLDERS
    # --------------------------------------------------

    st.markdown("---")

    st.subheader("👥 Key Stakeholders")

    stakeholder_df = pd.DataFrame({

        "Stakeholder":[
            "Manufacturer",
            "Supplier",
            "Warehouse",
            "Fulfillment Center",
            "Sorting Center",
            "Regional Hub",
            "Delivery Executive",
            "Customer Support",
            "Customer"
        ],

        "Primary Responsibility":[
            "Manufactures Products",
            "Supplies Inventory",
            "Stores Products",
            "Processes Orders",
            "Sorts Parcels",
            "Regional Distribution",
            "Delivers Orders",
            "Handles Customer Queries",
            "Receives Products"
        ]
    })

    st.dataframe(
        stakeholder_df,
        use_container_width=True
    )

    # --------------------------------------------------
    # MAJOR LAST MILE COMPANIES
    # --------------------------------------------------

    st.markdown("---")

    st.subheader("🏢 Major Last Mile Delivery Companies")

    companies_df = pd.DataFrame({

        "Company":[
            "Delhivery",
            "Blue Dart",
            "DTDC",
            "XpressBees",
            "Shadowfax",
            "Ecom Express",
            "Ekart",
            "Amazon Logistics",
            "DHL",
            "FedEx"
        ],

        "Country":[
            "India",
            "India",
            "India",
            "India",
            "India",
            "India",
            "India",
            "Global",
            "Global",
            "Global"
        ],

        "Specialization":[
            "E-Commerce Logistics",
            "Express Delivery",
            "Courier",
            "B2B & B2C",
            "Hyperlocal",
            "E-Commerce",
            "Flipkart Logistics",
            "Amazon Delivery",
            "International Logistics",
            "Express Logistics"
        ]
    })

    st.dataframe(
        companies_df,
        use_container_width=True
    )

    # --------------------------------------------------
    # DELIVERY TYPES
    # --------------------------------------------------

    st.markdown("---")

    st.subheader("🚚 Types of Last Mile Delivery")

    delivery_df = pd.DataFrame({

        "Delivery Type":[
            "Standard",
            "Express",
            "Same Day",
            "Next Day",
            "Hyperlocal",
            "Scheduled",
            "Cold Chain"
        ],

        "Typical Delivery Time":[
            "3-5 Days",
            "24 Hours",
            "Within 12 Hours",
            "Next Business Day",
            "30-90 Minutes",
            "Customer Preferred Time",
            "Temperature Controlled"
        ],

        "Common Industry":[
            "Retail",
            "Courier",
            "E-Commerce",
            "Retail",
            "Food & Grocery",
            "Furniture",
            "Healthcare"
        ]
    })

    st.dataframe(
        delivery_df,
        use_container_width=True
    )

    # --------------------------------------------------
    # DELIVERY VEHICLES
    # --------------------------------------------------

    st.markdown("---")

    st.subheader("🚛 Vehicles Used")

    vehicle_df = pd.DataFrame({

        "Vehicle":[
            "Motorcycle",
            "Scooter",
            "Mini Truck",
            "Van",
            "Electric Vehicle",
            "Bicycle",
            "Drone"
        ],

        "Primary Usage":[
            "Food Delivery",
            "Parcel Delivery",
            "Bulk Delivery",
            "Regional Distribution",
            "Eco-friendly Delivery",
            "Short Distance",
            "Future Deliveries"
        ]
    })

    st.dataframe(
        vehicle_df,
        use_container_width=True
    )

    # --------------------------------------------------
    # DELIVERY NETWORK
    # --------------------------------------------------

    st.markdown("---")

    st.subheader("🌐 Logistics Network Components")

    network_df = pd.DataFrame({

        "Component":[
            "Warehouse",
            "Fulfillment Center",
            "Sorting Center",
            "Regional Hub",
            "Micro Fulfillment Center",
            "Dark Store",
            "Delivery Hub",
            "Customer"
        ],

        "Purpose":[
            "Inventory Storage",
            "Order Processing",
            "Parcel Sorting",
            "Regional Distribution",
            "Fast Local Delivery",
            "Instant Grocery",
            "Assign Delivery Executive",
            "Receives Shipment"
        ]
    })

    st.dataframe(
        network_df,
        use_container_width=True
    )

    # --------------------------------------------------
    # DELIVERY PROCESS TIMELINE
    # --------------------------------------------------

    st.markdown("---")

    st.subheader("⏱ Typical Delivery Timeline")

    timeline_df = pd.DataFrame({

        "Stage":[
            "Order Placed",
            "Order Confirmed",
            "Warehouse Picking",
            "Packing",
            "Shipment Dispatch",
            "Out For Delivery",
            "Delivered"
        ],

        "Typical Time":[
            "0 min",
            "5-15 min",
            "30-90 min",
            "1-2 Hours",
            "2-5 Hours",
            "Same Day",
            "Customer Received"
        ]
    })

    st.dataframe(
        timeline_df,
        use_container_width=True
    )

    # --------------------------------------------------
    # ECOSYSTEM INSIGHTS
    # --------------------------------------------------

    st.markdown("---")

    st.subheader("📈 Ecosystem Insights")

    eco_col1, eco_col2 = st.columns(2)

    with eco_col1:

        st.success("""
### Strengths

✓ Fast Deliveries

✓ Real-time Tracking

✓ AI Powered Routing

✓ Mobile Workforce

✓ Digital Proof of Delivery

✓ Cloud Platforms
""")

    with eco_col2:

        st.warning("""
### Challenges

• Traffic Congestion

• Failed Deliveries

• Driver Shortage

• Fuel Cost

• Weather Impact

• Reverse Logistics
""")

    st.markdown("---")

    st.success("""
✅ Modern Last Mile Delivery depends on the seamless integration of Warehouses,
Fulfillment Centers, Delivery Hubs, Drivers, GPS, AI, Mobile Applications,
ERP, WMS and TMS systems.

Organizations with highly connected ecosystems achieve lower costs,
faster deliveries and higher customer satisfaction.
""")
    # ==================================================
    # LAST MILE TECHNOLOGY EXPLORER
    # ==================================================

    st.markdown("---")
    st.header("⚙️ Last Mile Technology Explorer")

    st.write("""
Explore the core technologies that power modern logistics companies.
Select a technology to understand its purpose, architecture,
business benefits, industry adoption and real-world usage.
""")

    technology = st.selectbox(
        "Select Technology",
        [
            "Enterprise Resource Planning (ERP)",
            "Warehouse Management System (WMS)",
            "Transportation Management System (TMS)",
            "Fleet Management System",
            "GPS Tracking"
        ]
    )

    # ==================================================
    # ERP
    # ==================================================

    if technology == "Enterprise Resource Planning (ERP)":

        st.subheader("🏢 Enterprise Resource Planning")

        col1, col2 = st.columns([3,1])

        with col1:

            st.info("""
Enterprise Resource Planning (ERP) integrates every department into one centralized system.

Main Modules

• Finance

• Procurement

• Inventory

• Human Resources

• Sales

• Customer Management

• Analytics

• Reporting
""")

        with col2:

            st.metric("Business Impact","95%")
            st.metric("Automation","90%")
            st.metric("Complexity","High")

        st.markdown("### 🌍 Popular ERP Solutions")

        erp_df = pd.DataFrame({

            "ERP":[
                "SAP S/4HANA",
                "Oracle ERP",
                "Microsoft Dynamics 365",
                "Odoo",
                "ERPNext"
            ],

            "Used By":[
                "Large Enterprises",
                "Global Logistics",
                "Medium & Large Businesses",
                "SMEs",
                "Growing Companies"
            ],

            "Cloud Support":[
                "Yes",
                "Yes",
                "Yes",
                "Yes",
                "Yes"
            ]
        })

        st.dataframe(
            erp_df,
            use_container_width=True
        )

        st.success("""
Business Benefits

✓ Single Source of Truth

✓ Better Decision Making

✓ Reduced Manual Work

✓ Financial Control

✓ Inventory Visibility

✓ Complete Business Integration
""")

        st.warning("""
Challenges

• High Cost

• Long Implementation

• User Training

• Customization Required
""")
    # ==================================================
    # WMS
    # ==================================================

    elif technology == "Warehouse Management System (WMS)":

        st.subheader("🏭 Warehouse Management System")

        st.info("""
Warehouse Management Systems manage warehouse operations.

Core Functions

• Goods Receiving

• Inventory Storage

• Picking

• Packing

• Shipping

• Barcode Management

• Stock Auditing
""")

        col1,col2,col3=st.columns(3)

        with col1:
            st.metric("Accuracy","99%")

        with col2:
            st.metric("Automation","85%")

        with col3:
            st.metric("Business Impact","90%")

        warehouse_df=pd.DataFrame({

            "Feature":[
                "Barcode",
                "RFID",
                "Inventory",
                "Picking",
                "Packing",
                "Shipping"
            ],

            "Supported":[
                "Yes",
                "Yes",
                "Yes",
                "Yes",
                "Yes",
                "Yes"
            ]
        })

        st.dataframe(
            warehouse_df,
            use_container_width=True
        )

        st.success("""
Benefits

✓ Inventory Accuracy

✓ Faster Picking

✓ Reduced Errors

✓ Better Warehouse Utilization
""")
    # ==================================================
    # TMS
    # ==================================================

    elif technology == "Transportation Management System (TMS)":

        st.subheader("🚚 Transportation Management System")

        st.info("""
Transportation Management Systems optimize transportation operations.

Capabilities

• Route Planning

• Carrier Selection

• Vehicle Assignment

• Shipment Tracking

• Freight Cost Optimization

• Delivery Scheduling
""")

        col1,col2,col3=st.columns(3)

        with col1:
            st.metric("Fuel Saving","18%")

        with col2:
            st.metric("Delivery Accuracy","96%")

        with col3:
            st.metric("Business Impact","92%")

        tms_df=pd.DataFrame({

            "Function":[
                "Route Planning",
                "Shipment Tracking",
                "Carrier Management",
                "Freight Billing",
                "ETA Prediction"
            ],

            "Automation":[
                "High",
                "High",
                "Medium",
                "High",
                "High"
            ]
        })

        st.dataframe(
            tms_df,
            use_container_width=True
        )

        st.success("""
Benefits

✓ Lower Transportation Cost

✓ Faster Deliveries

✓ Better Fleet Utilization

✓ Improved Customer Satisfaction
""")
    # ==================================================
    # FLEET
    # ==================================================

    elif technology == "Fleet Management System":

        st.subheader("🚛 Fleet Management")

        st.info("""
Fleet Management monitors vehicles, drivers and fuel usage.

Functions

• Vehicle Tracking

• Driver Behaviour

• Fuel Monitoring

• Vehicle Health

• Maintenance Scheduling
""")

        fleet_df=pd.DataFrame({

            "Feature":[
                "GPS",
                "Fuel",
                "Maintenance",
                "Dashcam",
                "Driver Score"
            ],

            "Availability":[
                "Yes",
                "Yes",
                "Yes",
                "Optional",
                "Yes"
            ]
        })

        st.dataframe(
            fleet_df,
            use_container_width=True
        )

        st.metric("Fleet Efficiency","89%")
    # ==================================================
    # GPS
    # ==================================================

    elif technology == "GPS Tracking":

        st.subheader("📍 GPS Tracking")

        st.info("""
GPS enables live vehicle monitoring and route visibility.

Applications

• Live Tracking

• ETA Prediction

• Theft Prevention

• Driver Monitoring

• Route Monitoring
""")

        gps_df=pd.DataFrame({

            "Capability":[
                "Live Tracking",
                "Geo Fencing",
                "Route Replay",
                "Alerts",
                "Speed Monitoring"
            ],

            "Supported":[
                "Yes",
                "Yes",
                "Yes",
                "Yes",
                "Yes"
            ]
        })

        st.dataframe(
            gps_df,
            use_container_width=True
        )

        st.metric("Tracking Accuracy","98%")

    # ==================================================
    # AI ROUTE OPTIMIZATION
    # ==================================================

    elif technology == "AI Route Optimization":

        st.subheader("🤖 AI Route Optimization")

        st.info("""
Artificial Intelligence optimizes delivery routes by analyzing real-time
traffic, weather, delivery priority, vehicle capacity and historical delivery data.

AI continuously recalculates routes to minimize delivery time and fuel consumption.
""")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Fuel Saving", "18%")

        with col2:
            st.metric("Delivery Speed", "+25%")

        with col3:
            st.metric("Business Impact", "97%")

        ai_df = pd.DataFrame({

            "AI Capability":[
                "Route Optimization",
                "Traffic Prediction",
                "ETA Prediction",
                "Demand Forecasting",
                "Driver Allocation",
                "Vehicle Scheduling"
            ],

            "Business Benefit":[
                "Lower Fuel Cost",
                "Avoid Congestion",
                "Customer Satisfaction",
                "Inventory Planning",
                "Balanced Workload",
                "Higher Utilization"
            ]

        })

        st.dataframe(ai_df, use_container_width=True)

        st.success("""
Business Benefits

✓ Faster Deliveries

✓ Lower Fuel Cost

✓ Better Driver Productivity

✓ Improved Customer Satisfaction

✓ Reduced Carbon Emission
""")

    # ==================================================
    # IoT
    # ==================================================

    elif technology == "IoT Sensors":

        st.subheader("📡 Internet of Things (IoT)")

        st.info("""
IoT sensors continuously monitor logistics assets in real time.

They help companies improve fleet health, shipment visibility,
cold-chain monitoring and predictive maintenance.
""")

        iot_df = pd.DataFrame({

            "Sensor":[
                "Temperature",
                "Humidity",
                "Fuel",
                "Door Status",
                "Tyre Pressure",
                "Engine Health",
                "Vehicle Location"
            ],

            "Purpose":[
                "Cold Chain",
                "Sensitive Goods",
                "Fuel Monitoring",
                "Security",
                "Safety",
                "Predictive Maintenance",
                "GPS Tracking"
            ]

        })

        st.dataframe(iot_df, use_container_width=True)

        st.metric("24x7 Monitoring", "Enabled")

        st.success("""
Business Benefits

✓ Real-time Monitoring

✓ Predictive Maintenance

✓ Reduced Breakdowns

✓ Better Asset Visibility
""")

    # ==================================================
    # RFID
    # ==================================================

    elif technology == "RFID & Barcode":

        st.subheader("🏷 RFID & Barcode")

        st.info("""
RFID and Barcode technologies uniquely identify every shipment
throughout the logistics network.

These technologies improve warehouse accuracy and parcel tracking.
""")

        rfid_df = pd.DataFrame({

            "Application":[
                "Inventory",
                "Warehouse",
                "Sorting",
                "Shipment Tracking",
                "Parcel Verification"
            ],

            "Technology":[
                "Barcode",
                "RFID",
                "RFID",
                "Barcode + RFID",
                "QR Code"
            ]

        })

        st.dataframe(rfid_df, use_container_width=True)

        st.metric("Scanning Accuracy", "99.8%")

        st.success("""
Advantages

✓ Faster Scanning

✓ Better Inventory Accuracy

✓ Reduced Human Error

✓ End-to-End Tracking
""")

    # ==================================================
    # MOBILE APP
    # ==================================================

    elif technology == "Mobile Delivery Application":

        st.subheader("📱 Delivery Executive Mobile Application")

        st.info("""
Delivery executives use mobile applications for
real-time delivery management.

These applications are connected with ERP, TMS and GPS systems.
""")

        app_df = pd.DataFrame({

            "Feature":[
                "Navigation",
                "Customer Calling",
                "OTP Verification",
                "QR Scanning",
                "Photo Upload",
                "Cash Collection",
                "Digital Signature",
                "ePOD"
            ],

            "Available":[
                "Yes",
                "Yes",
                "Yes",
                "Yes",
                "Yes",
                "Optional",
                "Yes",
                "Yes"
            ]

        })

        st.dataframe(app_df, use_container_width=True)

        st.metric("Daily Active Usage", "100%")

        st.success("""
Benefits

✓ Faster Delivery

✓ Better Communication

✓ Live Updates

✓ Digital Documentation
""")

    # ==================================================
    # DIGITAL PROOF OF DELIVERY
    # ==================================================

    elif technology == "Digital Proof of Delivery (ePOD)":

        st.subheader("✅ Electronic Proof of Delivery (ePOD)")

        st.info("""
Electronic Proof of Delivery confirms that a shipment
has been delivered successfully.

ePOD is completely paperless and integrates with ERP systems.
""")

        epod_df = pd.DataFrame({

            "Verification Method":[
                "OTP",
                "Digital Signature",
                "Customer Photo",
                "QR Code",
                "GPS Stamp",
                "Timestamp"
            ],

            "Purpose":[
                "Identity Verification",
                "Legal Confirmation",
                "Delivery Evidence",
                "Parcel Validation",
                "Location Verification",
                "Audit Trail"
            ]

        })

        st.dataframe(epod_df, use_container_width=True)

        st.metric("Paper Reduction", "100%")

        st.success("""
Benefits

✓ Fraud Prevention

✓ Paperless Operations

✓ Faster Confirmation

✓ Better Customer Trust

✓ Easy Auditing
""")
    
    
    # ==================================================
    # TECHNOLOGY MATURITY
    # ==================================================

    st.markdown("---")
    st.subheader("🏆 Technology Maturity Matrix")

    maturity_df = pd.DataFrame({

        "Technology":[
            "ERP",
            "WMS",
            "TMS",
            "Fleet",
            "GPS",
            "AI",
            "IoT",
            "RFID",
            "Mobile App",
            "ePOD"
        ],

        "Maturity":[
            "High",
            "High",
            "High",
            "Medium",
            "High",
            "Medium",
            "Growing",
            "Medium",
            "High",
            "High"
        ]

    })

    st.dataframe(
        maturity_df,
        use_container_width=True
    )

    # ==================================================
    # BUSINESS RECOMMENDATIONS
    # ==================================================

    st.markdown("---")
    st.subheader("💡 Business Recommendations")

    st.success("""
### Small Logistics Companies

• ERPNext / Odoo

• GPS Tracking

• Driver Mobile App

• Digital Proof of Delivery

----------------------------------------

### Medium Logistics Companies

• ERP

• WMS

• TMS

• Fleet Management

• GPS

• AI Route Planning

----------------------------------------

### Enterprise Logistics Companies

• SAP S/4HANA

• Oracle ERP

• AI Route Optimization

• IoT Sensors

• RFID

• Digital Twin

• Predictive Analytics

• Autonomous Warehouse
""")

    # ==================================================
    # FUTURE TECHNOLOGY ROADMAP
    # ==================================================

    st.markdown("---")
    st.subheader("🚀 Future Logistics Technology Roadmap")

    roadmap_df = pd.DataFrame({

        "Year":[
            2026,
            2027,
            2028,
            2029,
            2030
        ],

        "Emerging Technology":[
            "AI Everywhere",
            "Autonomous Delivery",
            "Digital Twin",
            "Warehouse Robotics",
            "Drone Deliveries"
        ]

    })

    st.dataframe(
        roadmap_df,
        use_container_width=True
    )

    roadmap_chart = px.line(
        roadmap_df,
        x="Year",
        y="Emerging Technology",
        markers=True,
        title="Future Logistics Technology Roadmap"
    )

    st.plotly_chart(
        roadmap_chart,
        use_container_width=True
    )

    # ==================================================
    # OVERALL TECHNOLOGY SCORECARD
    # ==================================================

    st.markdown("---")

    st.subheader("⭐ Overall Technology Scorecard")

    st.caption(
        "Assess the organization's overall technology readiness across key digital capabilities."
    )

    left_col, right_col = st.columns(2)

    with left_col:

        st.metric(label="Digital Transformation", value="92/100")
        st.progress(92)

        st.metric(label="Technology Adoption", value="88/100")
        st.progress(88)

        st.metric(label="Automation", value="90/100")
        st.progress(90)

    with right_col:

        st.metric(label="AI Readiness", value="86/100")
        st.progress(86)

        st.metric(label="Operational Visibility", value="91/100")
        st.progress(91)

        st.metric(label="Customer Experience", value="94/100")
        st.progress(94)

    st.info("""
### 📊 Score Guide

🟢 **90–100** : Excellent

🟡 **70–89** : Good

🟠 **50–69** : Moderate

🔴 **Below 50** : Needs Improvement
""")

    st.success("""
### 💡 Business Insight

The technology scorecard indicates a high level of digital maturity across
core logistics operations. Strong performance in customer experience,
digital transformation, and operational visibility demonstrates successful
technology adoption, while continued investment in AI capabilities will
further enhance business efficiency and competitive advantage.
""")
    # ==================================================
    # FINAL INSIGHT
    # ==================================================

    st.markdown("---")

    st.success("""
### 📌 Final Technology Insight

Modern logistics companies achieve the highest operational efficiency by integrating:

✅ ERP + WMS + TMS

✅ Fleet Management + GPS

✅ AI Route Optimization

✅ IoT Sensors

✅ Mobile Delivery Applications

✅ Digital Proof of Delivery

Companies investing in these technologies reduce operational costs,
improve customer satisfaction, enhance visibility and prepare themselves
for future innovations such as autonomous vehicles, warehouse robotics,
and drone-based deliveries.
""")
# ==============================
# 📌 Data Source Information
# ==============================

    import pandas as pd
    import streamlit as st

    st.markdown("---")
    st.subheader("📌 Data Source Information")

    # Read the Last Mile Delivery sheet
    df = pd.read_excel(
        "Data_Source.xlsx",      # Replace with your actual Excel file path
        sheet_name="Last mile delivery"
    )

    # Display only the required columns
    display_df = df[["Dashboard Component", "Data Type"]]

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )
# ==================================================
# COMPANY COMPARISON
# ==================================================

elif page == "⚖️ Company Comparison":

    st.header("⚖️ Company Comparison")

    # ----------------------------------------------
    # COMPANY SELECTION
    # ----------------------------------------------

    col1, col2 = st.columns(2)

    with col1:
        company1 = st.selectbox(
            "Select Company 1",
            companies["Company Name"],
            key="company1"
        )

    with col2:
        company2 = st.selectbox(
            "Select Company 2",
            companies["Company Name"],
            index=1 if len(companies) > 1 else 0,
            key="company2"
        )

    company1_data = companies[
        companies["Company Name"] == company1
    ].iloc[0]

    company2_data = companies[
        companies["Company Name"] == company2
    ].iloc[0]

    st.markdown("---")

    # ----------------------------------------------
    # QUICK KPI COMPARISON
    # ----------------------------------------------

    st.subheader("📊 Quick Comparison")

    col1, col2 = st.columns(2)

    with col1:

        st.success(company1)

        if "Technology Maturity" in companies.columns:
            st.metric(
                "Technology Maturity",
                company1_data["Technology Maturity"]
            )

        if "AI Readiness" in companies.columns:
            st.metric(
                "AI Readiness",
                company1_data["AI Readiness"]
            )

    with col2:

        st.success(company2)

        if "Technology Maturity" in companies.columns:
            st.metric(
                "Technology Maturity",
                company2_data["Technology Maturity"]
            )

        if "AI Readiness" in companies.columns:
            st.metric(
                "AI Readiness",
                company2_data["AI Readiness"]
            )

    st.markdown("---")

    # ----------------------------------------------
    # DETAILED COMPARISON TABLE
    # ----------------------------------------------

    st.subheader("📋 Detailed Comparison")

    comparison_df = pd.DataFrame({
        "Attribute": [
            "Industry",
            "Company Size",
            "Headquarters",
            "ERP System",
            "TMS System",
            "Fleet System",
            "Technology Maturity",
            "AI Readiness"
        ],
        company1: [
            company1_data.get("Industry", ""),
            company1_data.get("Company Size", ""),
            company1_data.get("Headquarters", ""),
            company1_data.get("ERP System", ""),
            company1_data.get("TMS System", ""),
            company1_data.get("Fleet System", ""),
            company1_data.get("Technology Maturity", ""),
            company1_data.get("AI Readiness", "")
        ],
        company2: [
            company2_data.get("Industry", ""),
            company2_data.get("Company Size", ""),
            company2_data.get("Headquarters", ""),
            company2_data.get("ERP System", ""),
            company2_data.get("TMS System", ""),
            company2_data.get("Fleet System", ""),
            company2_data.get("Technology Maturity", ""),
            company2_data.get("AI Readiness", "")
        ]
    })

    st.dataframe(
        comparison_df,
        use_container_width=True
    )

    st.markdown("---")

    # ----------------------------------------------
    # COMPARISON CHART
    # ----------------------------------------------

    st.subheader("📈 Technology Comparison")

    try:

        tech1 = float(company1_data["Technology Maturity"])
        ai1 = float(company1_data["AI Readiness"])

        tech2 = float(company2_data["Technology Maturity"])
        ai2 = float(company2_data["AI Readiness"])

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                name=company1,
                x=[
                    "Technology Maturity",
                    "AI Readiness"
                ],
                y=[
                    tech1,
                    ai1
                ]
            )
        )

        fig.add_trace(
            go.Bar(
                name=company2,
                x=[
                    "Technology Maturity",
                    "AI Readiness"
                ],
                y=[
                    tech2,
                    ai2
                ]
            )
        )

        fig.update_layout(
            barmode="group",
            title="Technology & AI Comparison"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    except:

        st.warning(
            "Technology Maturity and AI Readiness must be numeric values for chart comparison."
        )
# ==============================
# 📌 Data Source Information
# ==============================

    import pandas as pd
    import streamlit as st

    st.markdown("---")
    st.subheader("📌 Data Source Information")

    # Read the Company Comparison sheet
    df = pd.read_excel(
        "Data_Source.xlsx",      # Replace with your Excel file path
        sheet_name="company comparison"
    )

    # Display only the required columns
    display_df = df[["Dashboard Component", "Data Type"]]

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )
# ==================================================
# INSIGHTS & RECOMMENDATIONS
# ==================================================

elif page == "📈 Insights & Recommendations":

    st.header("📈 Insights & Recommendations")

    # ----------------------------------------------
    # PREPARE DATA
    # ----------------------------------------------

    temp_df = companies.copy()

    temp_df["AI Readiness"] = pd.to_numeric(
        temp_df["AI Readiness"],
        errors="coerce"
    )

    temp_df["Technology Maturity"] = pd.to_numeric(
        temp_df["Technology Maturity"],
        errors="coerce"
    )

    # ----------------------------------------------
    # TOP PERFORMERS
    # ----------------------------------------------

    ai_df = temp_df.dropna(subset=["AI Readiness"])
    tech_df = temp_df.dropna(subset=["Technology Maturity"])

    if len(ai_df) > 0:
        top_ai_company = ai_df.loc[
            ai_df["AI Readiness"].idxmax(),
            "Company Name"
        ]
    else:
        top_ai_company = "No Data"

    if len(tech_df) > 0:
        top_tech_company = tech_df.loc[
            tech_df["Technology Maturity"].idxmax(),
            "Company Name"
        ]
    else:
        top_tech_company = "No Data"

    most_used_system = (
        mapping["System Name"]
        .value_counts()
        .idxmax()
    )

    total_companies = len(companies)

    # ----------------------------------------------
    # KPI CARDS
    # ----------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Top AI Company", top_ai_company)

    with col2:
        st.metric("Top Tech Company", top_tech_company)

    with col3:
        st.metric("Most Used System", most_used_system)

    with col4:
        st.metric("Companies Analyzed", total_companies)

    st.markdown("---")

    # ----------------------------------------------
    # EXECUTIVE SUMMARY
    # ----------------------------------------------

    st.subheader("📌 Executive Summary")

    st.info(f"""
    • {top_ai_company} currently demonstrates the highest AI readiness.

    • {top_tech_company} has the most mature technology stack.

    • {most_used_system} is the most widely adopted system.

    • Enterprise organizations show higher digital maturity.

    • Companies investing in ERP + TMS integration generally score higher in technology readiness.
    """)

    # ----------------------------------------------
    # STRATEGIC RECOMMENDATIONS
    # ----------------------------------------------

    st.subheader("🚀 Strategic Recommendations")

    st.success("""
    1. Increase adoption of AI-powered route optimization.
    2. Expand warehouse automation initiatives.
    3. Integrate ERP, TMS and Fleet systems into a unified platform.
    4. Improve worker-facing mobile interfaces.
    5. Increase local language support for drivers and warehouse staff.
    6. Use predictive analytics for demand forecasting.
    7. Standardize operational data across all logistics functions.
    """)


    # ----------------------------------------------
    # TECHNOLOGY GAPS
    # ----------------------------------------------

    st.subheader("⚠️ Common Technology Gaps")

    st.info(f"""
    1. Legacy systems with outdated interfaces
    2. Limited AI implementation
    3. Manual reporting processes
    4. Poor integration between systems
    5. Low mobile usability for frontline workers
    6. Lack of multilingual support
    """)


    # ----------------------------------------------
    # HIGH IMPACT TECHNOLOGIES
    # ----------------------------------------------

    st.subheader("🏆 High Impact Technologies")

    impact_df = pd.DataFrame({
        "Technology": [
            "AI Route Optimization",
            "Predictive Analytics",
            "Warehouse Automation",
            "IoT Fleet Tracking",
            "Digital Twin Logistics"
        ],
        "Impact Score": [95, 90, 88, 85, 80]
    })

    impact_chart = px.bar(
        impact_df,
        x="Technology",
        y="Impact Score",
        title="Technology Impact Ranking"
    )

    st.plotly_chart(impact_chart, use_container_width=True)

    # ----------------------------------------------
    # FINAL CONCLUSION
    # ----------------------------------------------

    st.subheader("🎯 Final Conclusion")

    st.success(f"""
    The logistics industry is rapidly moving toward AI-driven operations.

    Among the analyzed companies, {top_ai_company} leads in AI readiness while {top_tech_company} demonstrates the strongest technology maturity.

    The most widely used platform is {most_used_system}, highlighting its importance in modern logistics operations.

    Future competitive advantage will come from stronger AI adoption, automation, predictive analytics and improved worker-facing technology.
    """)
# ==============================
# 📌 Data Source Information
# ==============================

    import pandas as pd
    import streamlit as st

    st.markdown("---")
    st.subheader("📌 Data Source Information")

    # Read the Insights & Recommendations sheet
    df = pd.read_excel(
        "Data_Source.xlsx",      # Replace with your Excel file path
        sheet_name="Insights_Recommendations"
    )

    # Display only the required columns
    display_df = df[["Dashboard Component", "Data Type"]]

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )