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

# ==================================================
# SYSTEM EXPLORER
# ==================================================

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
# ==================================================
# INSIGHTS & RECOMMENDATIONS
# ==================================================
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