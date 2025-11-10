# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.express as px
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots

# # Page configuration
# st.set_page_config(
#     page_title="Food Price Stability Dashboard",
#     page_icon="🌍",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS for better styling
# st.markdown("""
# <style>
#     .main-header {
#         font-size: 3rem;
#         color: #1f77b4;
#         text-align: center;
#         margin-bottom: 2rem;
#     }
#     .cluster-card {
#         padding: 1.5rem;
#         border-radius: 10px;
#         margin: 1rem 0;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#     }
#     .volatile-cluster {
#         background: linear-gradient(135deg, #ff6b6b, #ee5a24);
#         color: white;
#     }
#     .stable-cluster {
#         background: linear-gradient(135deg, #51cf66, #2f9e44);
#         color: white;
#     }
#     .metric-card {
#         background: #f8f9fa;
#         padding: 1rem;
#         border-radius: 10px;
#         border-left: 4px solid #1f77b4;
#     }
# </style>
# """, unsafe_allow_html=True)

# @st.cache_data
# def load_data():
#     results_df = pd.read_csv("food_price_clustering_results.csv")
#     return results_df  # Your existing results_df

# def main():
#     # Load data
#     df = load_data()
    
#     # Header
#     st.markdown('<h1 class="main-header">🌍 Food Price Stability Dashboard</h1>', unsafe_allow_html=True)
#     st.markdown("""
#     **UN SDG Indicator 2.c.1 Analysis** | Identifying patterns in food price volatility across countries
#     """)
    
#     # Sidebar
#     st.sidebar.title("🔍 Navigation")
#     page = st.sidebar.radio("Select Page:", [
#         "📊 Dashboard Overview",
#         "🌍 Interactive World Map", 
#         "📈 Cluster Analysis",
#         "🔬 Country Explorer",
#         "📋 Raw Data"
#     ])
    
#     # Page routing
#     if page == "📊 Dashboard Overview":
#         show_dashboard(df)
#     elif page == "🌍 Interactive World Map":
#         show_world_map(df)
#     elif page == "📈 Cluster Analysis":
#         show_cluster_analysis(df)
#     elif page == "🔬 Country Explorer":
#         show_country_explorer(df)
#     elif page == "📋 Raw Data":
#         show_raw_data(df)

# def show_dashboard(df):
#     """Main dashboard with key metrics and insights"""
    
#     st.header("📊 Executive Summary")
    
#     # Key metrics
#     col1, col2, col3, col4 = st.columns(4)
    
#     with col1:
#         st.metric("Total Countries", len(df))
    
#     with col2:
#         volatile_count = len(df[df['cluster_type'] == 'Volatile Markets'])
#         st.metric("Volatile Markets", volatile_count)
    
#     with col3:
#         stable_count = len(df[df['cluster_type'] == 'Stable Markets'])
#         st.metric("Stable Markets", stable_count)
    
#     with col4:
#         avg_volatility = df['volatility_std'].mean()
#         st.metric("Avg Volatility", f"{avg_volatility:.3f}")
    
#     # Cluster cards
#     st.header("🎯 Cluster Profiles")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown('<div class="cluster-card volatile-cluster">', unsafe_allow_html=True)
#         st.subheader("🔴 Volatile Markets")
#         volatile_df = df[df['cluster_type'] == 'Volatile Markets']
        
#         st.metric("Countries", len(volatile_df))
#         st.metric("Avg Volatility", f"{volatile_df['volatility_std'].mean():.3f}")
#         st.metric("Extreme Events", f"{volatile_df['extreme_positive_count'].mean():.1f}")
#         st.metric("Stability Score", f"{volatile_df['stability_inverse_volatility'].mean():.3f}")
        
#         st.markdown("**Top 5 Countries:**")
#         st.write(", ".join(volatile_df.head(5)['country'].tolist()))
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     with col2:
#         st.markdown('<div class="cluster-card stable-cluster">', unsafe_allow_html=True)
#         st.subheader("🟢 Stable Markets")
#         stable_df = df[df['cluster_type'] == 'Stable Markets']
        
#         st.metric("Countries", len(stable_df))
#         st.metric("Avg Volatility", f"{stable_df['volatility_std'].mean():.3f}")
#         st.metric("Extreme Events", f"{stable_df['extreme_positive_count'].mean():.1f}")
#         st.metric("Stability Score", f"{stable_df['stability_inverse_volatility'].mean():.3f}")
        
#         st.markdown("**Top 5 Countries:**")
#         st.write(", ".join(stable_df.head(5)['country'].tolist()))
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     # Key insights
#     st.header("💡 Key Insights")
    
#     insights_col1, insights_col2 = st.columns(2)
    
#     with insights_col1:
#         st.info("""
#         **🎯 Most Discriminating Features:**
#         - Volatility (2.6x higher in volatile markets)
#         - Extreme Events (4.2x more frequent)
#         - Stability Score (47% lower in volatile markets)
#         """)
        
#         st.success("""
#         **📊 Statistical Significance:**
#         - All key features: p < 0.0001
#         - Strong effect sizes (T-statistics > 6.0)
#         - Clear cluster separation
#         """)
    
#     with insights_col2:
#         st.warning("""
#         **🚨 Policy Priority - Volatile Markets:**
#         - Need immediate intervention
#         - Price stabilization required
#         - Social safety nets
#         - Supply chain diversification
#         """)
        
#         st.success("""
#         **🌟 Best Practices - Stable Markets:**
#         - Model for policy learning
#         - Knowledge sharing opportunities
#         - Maintain current systems
#         - Regional leadership
#         """)
    
#     # Feature comparison chart
#     st.header("📈 Feature Comparison")
    
#     fig = go.Figure()
    
#     features_to_compare = ['volatility_std', 'extreme_positive_count', 'stability_inverse_volatility']
#     feature_names = ['Volatility', 'Extreme Events', 'Stability Score']
    
#     for i, (feature, name) in enumerate(zip(features_to_compare, feature_names)):
#         volatile_mean = volatile_df[feature].mean()
#         stable_mean = stable_df[feature].mean()
        
#         fig.add_trace(go.Bar(
#             name=name,
#             x=['Volatile Markets', 'Stable Markets'],
#             y=[volatile_mean, stable_mean],
#             text=[f'{volatile_mean:.3f}', f'{stable_mean:.3f}'],
#             textposition='auto',
#             marker_color=['red', 'green']
#         ))
    
#     fig.update_layout(
#         title="Key Feature Comparison Between Clusters",
#         xaxis_title="Cluster Type",
#         yaxis_title="Average Value",
#         barmode='group'
#     )
    
#     st.plotly_chart(fig, use_container_width=True)

# def show_world_map(df):
#     """Interactive world map visualization"""
    
#     st.header("🌍 Global Food Price Stability Map")
    
#     # Create choropleth map
#     fig = px.choropleth(df,
#                         locations="country",
#                         locationmode="country names",
#                         color="cluster_type",
#                         hover_name="country",
#                         hover_data={
#                             'volatility_std': ':.3f',
#                             'extreme_positive_count': ':.1f',
#                             'stability_inverse_volatility': ':.3f',
#                             'cluster_type': False
#                         },
#                         title="Food Price Stability Clusters - Global Distribution",
#                         color_discrete_map={
#                             'Volatile Markets': 'red',
#                             'Stable Markets': 'green'
#                         })
    
#     fig.update_layout(
#         geo=dict(
#             showframe=False,
#             showcoastlines=True,
#             projection_type='equirectangular'
#         ),
#         height=600
#     )
    
#     st.plotly_chart(fig, use_container_width=True)
    
#     # Regional analysis
#     st.header("🗺️ Regional Analysis")
    
#     # Simple region classification (you might want to enhance this)
#     def get_region(country):
#         # Add your region mapping logic here
#         europe = ['Germany', 'France', 'Italy', 'Spain', 'United Kingdom', ...]
#         asia = ['China', 'India', 'Japan', 'South Korea', ...]
#         americas = ['United States', 'Brazil', 'Canada', 'Mexico', ...]
#         africa = ['Nigeria', 'South Africa', 'Egypt', 'Kenya', ...]
        
#         if country in europe:
#             return 'Europe'
#         elif country in asia:
#             return 'Asia'
#         elif country in americas:
#             return 'Americas'
#         elif country in africa:
#             return 'Africa'
#         else:
#             return 'Other'
    
#     df['region'] = df['country'].apply(get_region)
    
#     if 'region' in df.columns:
#         region_stats = df.groupby('region').agg({
#             'cluster_type': lambda x: (x == 'Volatile Markets').mean() * 100,
#             'volatility_std': 'mean',
#             'country': 'count'
#         }).round(2)
        
#         region_stats = region_stats.rename(columns={
#             'cluster_type': '% Volatile Markets',
#             'volatility_std': 'Avg Volatility',
#             'country': 'Country Count'
#         })
        
#         st.subheader("Regional Statistics")
#         st.dataframe(region_stats, use_container_width=True)

# def show_cluster_analysis(df):
#     """Detailed cluster analysis"""
    
#     st.header("📊 Detailed Cluster Analysis")
    
#     # Feature distributions
#     st.subheader("Feature Distributions by Cluster")
    
#     feature_to_analyze = st.selectbox(
#         "Select feature to analyze:",
#         ['volatility_std', 'extreme_positive_count', 'stability_inverse_volatility',
#          'extreme_negative_count', 'time_in_normal_range', 'recovery_speed']
#     )
    
#     fig = px.box(df, x='cluster_type', y=feature_to_analyze,
#                  color='cluster_type',
#                  color_discrete_map={'Volatile Markets': 'red', 'Stable Markets': 'green'})
    
#     fig.update_layout(
#         title=f"Distribution of {feature_to_analyze.replace('_', ' ').title()}",
#         xaxis_title="Cluster Type",
#         yaxis_title=feature_to_analyze.replace('_', ' ').title()
#     )
    
#     st.plotly_chart(fig, use_container_width=True)
    
#     # Statistical significance
#     st.subheader("🔬 Statistical Significance")
    
#     from scipy import stats
    
#     volatile_data = df[df['cluster_type'] == 'Volatile Markets'][feature_to_analyze]
#     stable_data = df[df['cluster_type'] == 'Stable Markets'][feature_to_analyze]
    
#     t_stat, p_value = stats.ttest_ind(volatile_data, stable_data)
    
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         st.metric("Volatile Markets Mean", f"{volatile_data.mean():.3f}")
#     with col2:
#         st.metric("Stable Markets Mean", f"{stable_data.mean():.3f}")
#     with col3:
#         st.metric("P-Value", f"{p_value:.6f}")
    
#     # Effect size visualization
#     st.subheader("Effect Size Visualization")
    
#     effect_size = (volatile_data.mean() - stable_data.mean()) / np.sqrt(
#         (volatile_data.std()**2 + stable_data.std()**2) / 2
#     )
    
#     fig_effect = go.Figure()
    
#     fig_effect.add_trace(go.Indicator(
#         mode = "gauge+number+delta",
#         value = abs(effect_size),
#         domain = {'x': [0, 1], 'y': [0, 1]},
#         title = {'text': f"Effect Size (Cohen's d)"},
#         gauge = {
#             'axis': {'range': [None, 2]},
#             'bar': {'color': "darkblue"},
#             'steps': [
#                 {'range': [0, 0.2], 'color': "lightgray"},
#                 {'range': [0.2, 0.5], 'color': "yellow"},
#                 {'range': [0.5, 0.8], 'color': "orange"},
#                 {'range': [0.8, 2], 'color': "red"}
#             ],
#             'threshold': {
#                 'line': {'color': "black", 'width': 4},
#                 'thickness': 0.75,
#                 'value': 0.8}
#         }
#     ))
    
#     st.plotly_chart(fig_effect, use_container_width=True)

# def show_country_explorer(df):
#     """Interactive country-level exploration"""
    
#     st.header("🔬 Country Explorer")
    
#     # Country selector
#     selected_country = st.selectbox("Select a country:", sorted(df['country'].unique()))
    
#     if selected_country:
#         country_data = df[df['country'] == selected_country].iloc[0]
        
#         st.subheader(f"📊 {selected_country} - Profile")
        
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             st.metric("Cluster", country_data['cluster_type'])
#             st.metric("Volatility", f"{country_data['volatility_std']:.3f}")
        
#         with col2:
#             st.metric("Extreme + Events", f"{country_data['extreme_positive_count']:.1f}")
#             st.metric("Extreme - Events", f"{country_data['extreme_negative_count']:.1f}")
        
#         with col3:
#             st.metric("Stability Score", f"{country_data['stability_inverse_volatility']:.3f}")
#             st.metric("Recovery Speed", f"{country_data['recovery_speed']:.3f}")
        
#         # Comparison with cluster averages
#         st.subheader("📈 Comparison with Cluster Averages")
        
#         cluster_avg = df[df['cluster_type'] == country_data['cluster_type']].mean(numeric_only=True)
        
#         comparison_data = {
#             'Metric': ['Volatility', 'Extreme Events', 'Stability Score'],
#             f'{selected_country}': [
#                 country_data['volatility_std'],
#                 country_data['extreme_positive_count'],
#                 country_data['stability_inverse_volatility']
#             ],
#             'Cluster Average': [
#                 cluster_avg['volatility_std'],
#                 cluster_avg['extreme_positive_count'],
#                 cluster_avg['stability_inverse_volatility']
#             ]
#         }
        
#         comparison_df = pd.DataFrame(comparison_data)
#         st.dataframe(comparison_df, use_container_width=True)
        
#         # Similar countries
#         st.subheader("🌍 Similar Countries")
        
#         same_cluster = df[df['cluster_type'] == country_data['cluster_type']]
#         similar_countries = same_cluster.nsmallest(6, 'volatility_std')['country'].tolist()
        
#         if selected_country in similar_countries:
#             similar_countries.remove(selected_country)
        
#         st.write(f"Countries with similar stability patterns: {', '.join(similar_countries[:5])}")

# def show_raw_data(df):
#     """Raw data explorer"""
    
#     st.header("📋 Raw Data Explorer")
    
#     # Data preview
#     st.subheader("Dataset Preview")
    
#     columns_to_show = st.multiselect(
#         "Select columns to display:",
#         df.columns.tolist(),
#         default=['country', 'cluster_type', 'volatility_std', 'extreme_positive_count', 'stability_inverse_volatility']
#     )
    
#     if columns_to_show:
#         st.dataframe(df[columns_to_show], use_container_width=True, height=400)
    
#     # Data statistics
#     st.subheader("Dataset Statistics")
#     st.write(df.describe())
    
#     # Download options
#     st.subheader("📥 Download Data")
    
#     csv = df.to_csv(index=False)
#     st.download_button(
#         label="Download Full Dataset as CSV",
#         data=csv,
#         file_name="food_price_stability_clusters.csv",
#         mime="text/csv"
#     )

# if __name__ == "__main__":
#     # Load your data (replace with your actual data loading)
#     # For now, we'll assume results_df is available
#     try:
#         main()
#     except NameError:
#         st.error("⚠️ Please ensure 'results_df' is available in your environment.")
#         st.info("Replace the load_data() function with your actual data loading logic.")
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import tensorflow as tf
# Then use tf.keras.models.load_model() in your code
import joblib
import json


# Page configuration
st.set_page_config(
    page_title="Food Price Stability Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .cluster-card {
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .volatile-cluster {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
    }
    .stable-cluster {
        background: linear-gradient(135deg, #51cf66, #2f9e44);
        color: white;
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
    }
    .prediction-card {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    results_df = pd.read_csv("food_price_clustering_results.csv")
    return results_df

# Load preprocessing objects and model
@st.cache_resource
# def load_preprocessing():
#     try:
#         scaler = joblib.load('scaler.pkl')
#         pca = joblib.load('pca.pkl')
#         with open('feature_columns.json', 'r') as f:
#             feature_columns = json.load(f)
#         model = tf.keras.models.load_model('food_price_classifier')
#         return model, scaler, pca, feature_columns
#     except Exception as e:
#         st.error(f"Error loading model/preprocessing: {e}")
#         return None, None, None, None
def load_preprocessing():
    try:
        import os
        st.info("🔍 Starting to load preprocessing objects...")
        
        # Check if files exist
        st.write("Checking file existence:")
        st.write(f"- scaler.pkl: {os.path.exists('scaler.pkl')}")
        st.write(f"- pca.pkl: {os.path.exists('pca.pkl')}")
        st.write(f"- feature_columns.json: {os.path.exists('feature_columns.json')}")
        st.write(f"- food_price_classifier folder: {os.path.exists('food_price_classifier')}")
        
        # Load preprocessing objects
        scaler = joblib.load('scaler.pkl')
        st.success("✅ Scaler loaded")
        
        pca = joblib.load('pca.pkl')
        st.success("✅ PCA loaded")
        
        with open('feature_columns.json', 'r') as f:
            feature_columns = json.load(f)
        st.success("✅ Feature columns loaded")
        
        # Try loading model with different formats
        st.info("🔄 Attempting to load model...")
        
        # Check what model files actually exist
        if os.path.exists('food_price_classifier'):
            st.write("Found SavedModel folder, loading...")
            model = tf.keras.models.load_model('food_price_classifier')
        elif os.path.exists('food_price_classifier.h5'):
            st.write("Found .h5 file, loading...")
            model = tf.keras.models.load_model('food_price_classifier.h5')
        elif os.path.exists('food_price_classifier.keras'):
            st.write("Found .keras file, loading...")
            model = tf.keras.models.load_model('food_price_classifier.keras')
        else:
            st.error("❌ No model file found!")
            return None, None, None, None
            
        st.success("✅ Model loaded successfully!")
        return model, scaler, pca, feature_columns
        
    except Exception as e:
        st.error(f"❌ Error loading model/preprocessing: {str(e)}")
        import traceback
        st.code(traceback.format_exc())
        return None, None, None, None

def predict_new_country(model, scaler, pca, new_data, feature_columns):
    """Predict cluster for new country data using both scaler and PCA"""
    # model, scaler, pca, feature_columns = load_preprocessing()
    
    # Ensure new_data has the same features
    if isinstance(new_data, dict):
        new_df = pd.DataFrame([new_data])
        # Ensure all feature columns are present
        for col in feature_columns:
            if col not in new_df.columns:
                new_df[col] = 0  # Or appropriate default value
        
        # Apply the same preprocessing pipeline
        new_data_scaled = scaler.transform(new_df[feature_columns])
        new_data_pca = pca.transform(new_data_scaled)
    else:
        new_data_scaled = scaler.transform(new_data.reshape(1, -1))
        new_data_pca = pca.transform(new_data_scaled)
    
    # Predict
    prediction_proba = model.predict(new_data_pca, verbose=0)
    predicted_cluster = np.argmax(prediction_proba, axis=1)[0]
    confidence = np.max(prediction_proba)
    
    return predicted_cluster, confidence, prediction_proba[0]

def main():
    # Load data and model
    df = load_data()
    model, scaler, pca, feature_columns = load_preprocessing()
    
    # Header
    st.markdown('<h1 class="main-header">🌍 Food Price Stability Dashboard</h1>', unsafe_allow_html=True)
    st.markdown("""
    **UN SDG Indicator 2.c.1 Analysis** | Identifying patterns in food price volatility across countries
    """)
    
    # Sidebar
    st.sidebar.title("🔍 Navigation")
    page = st.sidebar.radio("Select Page:", [
        "📊 Dashboard Overview",
        "🌍 Interactive World Map", 
        "📈 Cluster Analysis",
        "🔬 Country Explorer",
        "🎯 Predict New Country",
        "📋 Raw Data"
    ])
    
    # Page routing
    if page == "📊 Dashboard Overview":
        show_dashboard(df)
    elif page == "🌍 Interactive World Map":
        show_world_map(df)
    elif page == "📈 Cluster Analysis":
        show_cluster_analysis(df)
    elif page == "🔬 Country Explorer":
        show_country_explorer(df)
    elif page == "🎯 Predict New Country":
        show_prediction_interface(model, scaler, pca, feature_columns, df)
    elif page == "📋 Raw Data":
        show_raw_data(df)

# def show_prediction_interface(model, scaler, pca, feature_columns, df):
#     # model = "food_price_classifier.h5"
#     # df = load_data()
#     df = load_data()
#     model, scaler, pca, feature_columns = load_preprocessing()
#     """Interface for predicting clusters for new countries"""
    
#     st.header("🎯 Predict New Country Cluster")
    
#     if model is None or scaler is None or pca is None:
#         st.error("⚠️ Model or preprocessing objects not loaded. Please ensure all files are available:")
#         st.info("Required files: cluster_model.h5, scaler.pkl, pca.pkl, feature_columns.json")
#         return
    
#     st.markdown("""
#     Enter the food price stability metrics for a new country to predict which cluster it belongs to.
#     The model will classify it as either **Volatile Markets** or **Stable Markets**.
#     """)
    
#     # Create input form
#     st.subheader("📊 Enter Country Metrics")
    
#     input_data = {}
    
#     # Create columns for better organization
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         input_data['volatility_std'] = st.number_input(
#             "Volatility (Standard Deviation)", 
#             min_value=0.0, 
#             max_value=10.0, 
#             value=1.0,
#             help="Standard deviation of price changes"
#         )
        
#         input_data['extreme_positive_count'] = st.number_input(
#             "Extreme Positive Events Count", 
#             min_value=0.0, 
#             max_value=100.0, 
#             value=5.0,
#             help="Number of extreme positive price spikes"
#         )
        
#         input_data['max_positive_extreme'] = st.number_input(
#             "Maximum Positive Extreme", 
#             min_value=0.0, 
#             max_value=50.0, 
#             value=2.0,
#             help="Largest positive price spike observed"
#         )
    
#     with col2:
#         input_data['extreme_negative_count'] = st.number_input(
#             "Extreme Negative Events Count", 
#             min_value=0.0, 
#             max_value=100.0, 
#             value=3.0,
#             help="Number of extreme negative price drops"
#         )
        
#         input_data['stability_inverse_volatility'] = st.number_input(
#             "Stability Score", 
#             min_value=0.0, 
#             max_value=10.0, 
#             value=0.5,
#             help="Inverse volatility measure (higher = more stable)"
#         )
        
#         input_data['time_in_normal_range'] = st.number_input(
#             "Time in Normal Range (%)", 
#             min_value=0.0, 
#             max_value=1.0, 
#             value=0.8,
#             help="Proportion of time prices are in normal range (0-1)"
#         )
    
#     with col3:
#         input_data['recovery_speed'] = st.number_input(
#             "Recovery Speed", 
#             min_value=0.0, 
#             max_value=10.0, 
#             value=1.0,
#             help="Speed of recovery from price shocks"
#         )
        
#         # Add any additional features your model expects
#         # Example: if you have more features, add them here
#         # input_data['additional_feature'] = st.number_input("Additional Feature", value=0.0)
    
#     # Country name input
#     country_name = st.text_input("Country Name (Optional)", placeholder="Enter country name for reference")
    
#     # Prediction button
#     if st.button("🎯 Predict Cluster", type="primary"):
#         with st.spinner("Analyzing country metrics..."):
#             try:
#                 # Make prediction
#                 cluster, confidence, probabilities = predict_new_country(
#                     model, scaler, pca, input_data, feature_columns
#                 )
                
#                 # Display results
#                 st.markdown("---")
#                 st.markdown('<div class="prediction-card">', unsafe_allow_html=True)
                
#                 # Determine cluster type
#                 cluster_type = "Volatile Markets" if cluster == 1 else "Stable Markets"
#                 cluster_color = "🔴" if cluster == 1 else "🟢"
                
#                 st.subheader(f"{cluster_color} Prediction Results")
                
#                 col1, col2, col3 = st.columns(3)
                
#                 with col1:
#                     st.metric("Predicted Cluster", cluster_type)
                
#                 with col2:
#                     st.metric("Confidence", f"{confidence:.1%}")
                
#                 with col3:
#                     st.metric("Cluster ID", cluster)
                
#                 st.markdown('</div>', unsafe_allow_html=True)
                
#                 # Probability breakdown
#                 st.subheader("📊 Probability Breakdown")
                
#                 prob_df = pd.DataFrame({
#                     'Cluster': ['Stable Markets', 'Volatile Markets'],
#                     'Probability': [probabilities[0], probabilities[1]]
#                 })
                
#                 fig = px.bar(prob_df, x='Cluster', y='Probability', 
#                             color='Cluster',
#                             color_discrete_map={
#                                 'Stable Markets': 'green',
#                                 'Volatile Markets': 'red'
#                             },
#                             text_auto='.1%')
                
#                 fig.update_layout(
#                     title="Cluster Probability Distribution",
#                     yaxis_tickformat='.0%',
#                     showlegend=False
#                 )
                
#                 st.plotly_chart(fig, use_container_width=True)
                
#                 # Interpretation
#                 st.subheader("💡 Interpretation")
                
#                 if cluster_type == "Volatile Markets":
#                     st.warning("""
#                     **🔴 Volatile Markets Profile:**
#                     - Higher price volatility and uncertainty
#                     - More frequent extreme price events
#                     - May require policy intervention
#                     - Potential food security concerns
#                     """)
#                 else:
#                     st.success("""
#                     **🟢 Stable Markets Profile:**
#                     - Lower price volatility
#                     - More predictable food prices
#                     - Stronger market regulation
#                     - Better food security outcomes
#                     """)
                
#                 # Similar countries from existing data
#                 st.subheader("🌍 Similar Countries in Dataset")
                
#                 similar_cluster_df = df[df['cluster'] == cluster]
#                 if not similar_cluster_df.empty:
#                     similar_countries = similar_cluster_df.nsmallest(
#                         5, 
#                         'volatility_std'
#                     )['country'].tolist()
                    
#                     st.write(f"Countries with similar characteristics: {', '.join(similar_countries)}")
                
#             except Exception as e:
#                 st.error(f"Prediction error: {e}")
#                 st.info("Please check that all required feature values are provided.")
def show_prediction_interface(model, scaler, pca, feature_columns, df):
    """Interface for predicting clusters for new countries"""
    
    st.header("🎯 Predict New Country Cluster")
    
    if model is None or scaler is None or pca is None:
        st.error("⚠️ Model or preprocessing objects not loaded. Please ensure all files are available:")
        st.info("Required files: cluster_model.h5, scaler.pkl, pca.pkl, feature_columns.json")
        return
    
    st.markdown("""
    Enter the food price stability metrics for a new country to predict which cluster it belongs to.
    The model will classify it as either **Volatile Markets** or **Stable Markets**.
    """)
    
    # Create input form
    st.subheader("📊 Enter Country Metrics")
    
    input_data = {}
    
    # Create columns for better organization
    col1, col2, col3 = st.columns(3)
    
    with col1:
        input_data['volatility_std'] = st.number_input(
            "Volatility (Standard Deviation)", 
            min_value=0.0, 
            max_value=10.0, 
            value=1.0,
            help="Standard deviation of price changes"
        )
        
        input_data['extreme_positive_count'] = st.number_input(
            "Extreme Positive Events Count", 
            min_value=0.0, 
            max_value=100.0, 
            value=5.0,
            help="Number of extreme positive price spikes"
        )
        
        input_data['max_positive_extreme'] = st.number_input(
            "Maximum Positive Extreme", 
            min_value=0.0, 
            max_value=50.0, 
            value=2.0,
            help="Largest positive price spike observed"
        )
        
        input_data['high_volatility_periods'] = st.number_input(
            "High Volatility Periods", 
            min_value=0.0, 
            max_value=100.0, 
            value=2.0,
            help="Number of high volatility periods"
        )
    
    with col2:
        input_data['extreme_negative_count'] = st.number_input(
            "Extreme Negative Events Count", 
            min_value=0.0, 
            max_value=100.0, 
            value=3.0,
            help="Number of extreme negative price drops"
        )
        
        input_data['stability_inverse_volatility'] = st.number_input(
            "Stability Score", 
            min_value=0.0, 
            max_value=10.0, 
            value=0.5,
            help="Inverse volatility measure (higher = more stable)"
        )
        
        input_data['time_in_normal_range'] = st.number_input(
            "Time in Normal Range (%)", 
            min_value=0.0, 
            max_value=1.0, 
            value=0.8,
            help="Proportion of time prices are in normal range (0-1)"
        )
        
        input_data['crisis_events'] = st.number_input(
            "Crisis Events", 
            min_value=0.0, 
            max_value=50.0, 
            value=1.0,
            help="Number of crisis-level events"
        )
    
    with col3:
        input_data['recovery_speed'] = st.number_input(
            "Recovery Speed", 
            min_value=0.0, 
            max_value=10.0, 
            value=1.0,
            help="Speed of recovery from price shocks"
        )
        
        input_data['total_extreme_events'] = st.number_input(
            "Total Extreme Events", 
            min_value=0.0, 
            max_value=150.0, 
            value=8.0,
            help="Total number of extreme events (positive + negative)"
        )
        
        input_data['max_negative_extreme'] = st.number_input(
            "Maximum Negative Extreme", 
            min_value=-50.0, 
            max_value=0.0, 
            value=-1.5,
            help="Largest negative price drop observed"
        )
        
        input_data['avg_extreme_magnitude'] = st.number_input(
            "Average Extreme Magnitude", 
            min_value=0.0, 
            max_value=25.0, 
            value=1.2,
            help="Average magnitude of extreme events"
        )
        
        input_data['consistency_score'] = st.number_input(
            "Consistency Score", 
            min_value=0.0, 
            max_value=10.0, 
            value=0.7,
            help="Price consistency score (higher = more consistent)"
        )
    
    # Country name input
    country_name = st.text_input("Country Name (Optional)", placeholder="Enter country name for reference")
    
    # Prediction button
    if st.button("🎯 Predict Cluster", type="primary"):
        with st.spinner("Analyzing country metrics..."):
            try:
                # Make prediction
                cluster, confidence, probabilities = predict_new_country(
                    model, scaler, pca, input_data, feature_columns
                )
                
                # Display results
                st.markdown("---")
                st.markdown('<div class="prediction-card">', unsafe_allow_html=True)
                
                # Determine cluster type
                cluster_type = "Volatile Markets" if cluster == 1 else "Stable Markets"
                cluster_color = "🔴" if cluster == 1 else "🟢"
                
                st.subheader(f"{cluster_color} Prediction Results")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Predicted Cluster", cluster_type)
                
                with col2:
                    st.metric("Confidence", f"{confidence:.1%}")
                
                with col3:
                    st.metric("Cluster ID", cluster)
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Probability breakdown
                st.subheader("📊 Probability Breakdown")
                
                prob_df = pd.DataFrame({
                    'Cluster': ['Stable Markets', 'Volatile Markets'],
                    'Probability': [probabilities[0], probabilities[1]]
                })
                
                fig = px.bar(prob_df, x='Cluster', y='Probability', 
                            color='Cluster',
                            color_discrete_map={
                                'Stable Markets': 'green',
                                'Volatile Markets': 'red'
                            },
                            text_auto='.1%')
                
                fig.update_layout(
                    title="Cluster Probability Distribution",
                    yaxis_tickformat='.0%',
                    showlegend=False
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Interpretation
                st.subheader("💡 Interpretation")
                
                if cluster_type == "Volatile Markets":
                    st.warning("""
                    **🔴 Volatile Markets Profile:**
                    - Higher price volatility and uncertainty
                    - More frequent extreme price events
                    - May require policy intervention
                    - Potential food security concerns
                    """)
                else:
                    st.success("""
                    **🟢 Stable Markets Profile:**
                    - Lower price volatility
                    - More predictable food prices
                    - Stronger market regulation
                    - Better food security outcomes
                    """)
                
                # Similar countries from existing data
                st.subheader("🌍 Similar Countries in Dataset")
                
                similar_cluster_df = df[df['cluster'] == cluster]
                if not similar_cluster_df.empty:
                    similar_countries = similar_cluster_df.nsmallest(
                        5, 
                        'volatility_std'
                    )['country'].tolist()
                    
                    st.write(f"Countries with similar characteristics: {', '.join(similar_countries)}")
                
            except Exception as e:
                st.error(f"Prediction error: {e}")
                st.info("Please check that all required feature values are provided.") 
    # Feature descriptions
    with st.expander("📖 Feature Descriptions"):
        st.markdown("""
        **Feature Definitions:**
        - **Volatility**: Standard deviation of price changes (higher = more volatile)
        - **High Volatility Periods**: Number of periods with exceptionally high volatility
        - **Extreme Positive Events**: Count of large price spikes
        - **Extreme Negative Events**: Count of large price drops  
        - **Crisis Events**: Number of crisis-level price events
        - **Total Extreme Events**: Sum of all extreme events (positive + negative)
        - **Max Positive Extreme**: Largest positive price spike observed
        - **Max Negative Extreme**: Largest negative price drop observed
        - **Avg Extreme Magnitude**: Average size of extreme events
        - **Stability Score**: Inverse volatility measure (higher = more stable)
        - **Time in Normal Range**: Percentage of time prices are within normal bounds
        - **Recovery Speed**: How quickly prices return to normal after shocks
        - **Consistency Score**: Measure of price consistency over time
        """)
# Your existing functions remain the same below...
def show_dashboard(df):
    """Main dashboard with key metrics and insights"""
    
    st.header("📊 Executive Summary")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Countries", len(df))
    
    with col2:
        volatile_count = len(df[df['cluster_type'] == 'Volatile Markets'])
        st.metric("Volatile Markets", volatile_count)
    
    with col3:
        stable_count = len(df[df['cluster_type'] == 'Stable Markets'])
        st.metric("Stable Markets", stable_count)
    
    with col4:
        avg_volatility = df['volatility_std'].mean()
        st.metric("Avg Volatility", f"{avg_volatility:.3f}")
    
    # Cluster cards
    st.header("🎯 Cluster Profiles")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="cluster-card volatile-cluster">', unsafe_allow_html=True)
        st.subheader("🔴 Volatile Markets")
        volatile_df = df[df['cluster_type'] == 'Volatile Markets']
        
        st.metric("Countries", len(volatile_df))
        st.metric("Avg Volatility", f"{volatile_df['volatility_std'].mean():.3f}")
        st.metric("Extreme Events", f"{volatile_df['extreme_positive_count'].mean():.1f}")
        st.metric("Stability Score", f"{volatile_df['stability_inverse_volatility'].mean():.3f}")
        
        st.markdown("**Top 5 Countries:**")
        st.write(", ".join(volatile_df.head(5)['country'].tolist()))
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="cluster-card stable-cluster">', unsafe_allow_html=True)
        st.subheader("🟢 Stable Markets")
        stable_df = df[df['cluster_type'] == 'Stable Markets']
        
        st.metric("Countries", len(stable_df))
        st.metric("Avg Volatility", f"{stable_df['volatility_std'].mean():.3f}")
        st.metric("Extreme Events", f"{stable_df['extreme_positive_count'].mean():.1f}")
        st.metric("Stability Score", f"{stable_df['stability_inverse_volatility'].mean():.3f}")
        
        st.markdown("**Top 5 Countries:**")
        st.write(", ".join(stable_df.head(5)['country'].tolist()))
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Key insights
    st.header("💡 Key Insights")
    
    insights_col1, insights_col2 = st.columns(2)
    
    with insights_col1:
        st.info("""
        **🎯 Most Discriminating Features:**
        - Volatility (2.6x higher in volatile markets)
        - Extreme Events (4.2x more frequent)
        - Stability Score (47% lower in volatile markets)
        """)
        
        st.success("""
        **📊 Statistical Significance:**
        - All key features: p < 0.0001
        - Strong effect sizes (T-statistics > 6.0)
        - Clear cluster separation
        """)
    
    with insights_col2:
        st.warning("""
        **🚨 Policy Priority - Volatile Markets:**
        - Need immediate intervention
        - Price stabilization required
        - Social safety nets
        - Supply chain diversification
        """)
        
        st.success("""
        **🌟 Best Practices - Stable Markets:**
        - Model for policy learning
        - Knowledge sharing opportunities
        - Maintain current systems
        - Regional leadership
        """)
    
    # Feature comparison chart
    st.header("📈 Feature Comparison")
    
    fig = go.Figure()
    
    features_to_compare = ['volatility_std', 'extreme_positive_count', 'stability_inverse_volatility']
    feature_names = ['Volatility', 'Extreme Events', 'Stability Score']
    
    for i, (feature, name) in enumerate(zip(features_to_compare, feature_names)):
        volatile_mean = volatile_df[feature].mean()
        stable_mean = stable_df[feature].mean()
        
        fig.add_trace(go.Bar(
            name=name,
            x=['Volatile Markets', 'Stable Markets'],
            y=[volatile_mean, stable_mean],
            text=[f'{volatile_mean:.3f}', f'{stable_mean:.3f}'],
            textposition='auto',
            marker_color=['red', 'green']
        ))
    
    fig.update_layout(
        title="Key Feature Comparison Between Clusters",
        xaxis_title="Cluster Type",
        yaxis_title="Average Value",
        barmode='group'
    )
    
    st.plotly_chart(fig, use_container_width=True)

def show_world_map(df):
    """Interactive world map visualization"""
    
    st.header("🌍 Global Food Price Stability Map")
    
    # Create choropleth map
    fig = px.choropleth(df,
                        locations="country",
                        locationmode="country names",
                        color="cluster_type",
                        hover_name="country",
                        hover_data={
                            'volatility_std': ':.3f',
                            'extreme_positive_count': ':.1f',
                            'stability_inverse_volatility': ':.3f',
                            'cluster_type': False
                        },
                        title="Food Price Stability Clusters - Global Distribution",
                        color_discrete_map={
                            'Volatile Markets': 'red',
                            'Stable Markets': 'green'
                        })
    
    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type='equirectangular'
        ),
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Regional analysis
    st.header("🗺️ Regional Analysis")
    
    # Simple region classification (you might want to enhance this)
    def get_region(country):
        # Add your region mapping logic here
        europe = ['Germany', 'France', 'Italy', 'Spain', 'United Kingdom']
        asia = ['China', 'India', 'Japan', 'South Korea']
        americas = ['United States', 'Brazil', 'Canada', 'Mexico']
        africa = ['Nigeria', 'South Africa', 'Egypt', 'Kenya']
        
        if country in europe:
            return 'Europe'
        elif country in asia:
            return 'Asia'
        elif country in americas:
            return 'Americas'
        elif country in africa:
            return 'Africa'
        else:
            return 'Other'
    
    df['region'] = df['country'].apply(get_region)
    
    if 'region' in df.columns:
        region_stats = df.groupby('region').agg({
            'cluster_type': lambda x: (x == 'Volatile Markets').mean() * 100,
            'volatility_std': 'mean',
            'country': 'count'
        }).round(2)
        
        region_stats = region_stats.rename(columns={
            'cluster_type': '% Volatile Markets',
            'volatility_std': 'Avg Volatility',
            'country': 'Country Count'
        })
        
        st.subheader("Regional Statistics")
        st.dataframe(region_stats, use_container_width=True)

def show_cluster_analysis(df):
    """Detailed cluster analysis"""
    
    st.header("📊 Detailed Cluster Analysis")
    
    # Feature distributions
    st.subheader("Feature Distributions by Cluster")
    
    feature_to_analyze = st.selectbox(
        "Select feature to analyze:",
        ['volatility_std', 'extreme_positive_count', 'stability_inverse_volatility',
         'extreme_negative_count', 'time_in_normal_range', 'recovery_speed']
    )
    
    fig = px.box(df, x='cluster_type', y=feature_to_analyze,
                 color='cluster_type',
                 color_discrete_map={'Volatile Markets': 'red', 'Stable Markets': 'green'})
    
    fig.update_layout(
        title=f"Distribution of {feature_to_analyze.replace('_', ' ').title()}",
        xaxis_title="Cluster Type",
        yaxis_title=feature_to_analyze.replace('_', ' ').title()
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Statistical significance
    st.subheader("🔬 Statistical Significance")
    
    from scipy import stats
    
    volatile_data = df[df['cluster_type'] == 'Volatile Markets'][feature_to_analyze]
    stable_data = df[df['cluster_type'] == 'Stable Markets'][feature_to_analyze]
    
    t_stat, p_value = stats.ttest_ind(volatile_data, stable_data)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Volatile Markets Mean", f"{volatile_data.mean():.3f}")
    with col2:
        st.metric("Stable Markets Mean", f"{stable_data.mean():.3f}")
    with col3:
        st.metric("P-Value", f"{p_value:.6f}")
    
    # Effect size visualization
    st.subheader("Effect Size Visualization")
    
    effect_size = (volatile_data.mean() - stable_data.mean()) / np.sqrt(
        (volatile_data.std()**2 + stable_data.std()**2) / 2
    )
    
    fig_effect = go.Figure()
    
    fig_effect.add_trace(go.Indicator(
        mode = "gauge+number+delta",
        value = abs(effect_size),
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': f"Effect Size (Cohen's d)"},
        gauge = {
            'axis': {'range': [None, 2]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 0.2], 'color': "lightgray"},
                {'range': [0.2, 0.5], 'color': "yellow"},
                {'range': [0.5, 0.8], 'color': "orange"},
                {'range': [0.8, 2], 'color': "red"}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': 0.8}
        }
    ))
    
    st.plotly_chart(fig_effect, use_container_width=True)

def show_country_explorer(df):
    """Interactive country-level exploration"""
    
    st.header("🔬 Country Explorer")
    
    # Country selector
    selected_country = st.selectbox("Select a country:", sorted(df['country'].unique()))
    
    if selected_country:
        country_data = df[df['country'] == selected_country].iloc[0]
        
        st.subheader(f"📊 {selected_country} - Profile")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Cluster", country_data['cluster_type'])
            st.metric("Volatility", f"{country_data['volatility_std']:.3f}")
        
        with col2:
            st.metric("Extreme + Events", f"{country_data['extreme_positive_count']:.1f}")
            st.metric("Extreme - Events", f"{country_data['extreme_negative_count']:.1f}")
        
        with col3:
            st.metric("Stability Score", f"{country_data['stability_inverse_volatility']:.3f}")
            st.metric("Recovery Speed", f"{country_data['recovery_speed']:.3f}")
        
        # Comparison with cluster averages
        st.subheader("📈 Comparison with Cluster Averages")
        
        cluster_avg = df[df['cluster_type'] == country_data['cluster_type']].mean(numeric_only=True)
        
        comparison_data = {
            'Metric': ['Volatility', 'Extreme Events', 'Stability Score'],
            f'{selected_country}': [
                country_data['volatility_std'],
                country_data['extreme_positive_count'],
                country_data['stability_inverse_volatility']
            ],
            'Cluster Average': [
                cluster_avg['volatility_std'],
                cluster_avg['extreme_positive_count'],
                cluster_avg['stability_inverse_volatility']
            ]
        }
        
        comparison_df = pd.DataFrame(comparison_data)
        st.dataframe(comparison_df, use_container_width=True)
        
        # Similar countries
        st.subheader("🌍 Similar Countries")
        
        same_cluster = df[df['cluster_type'] == country_data['cluster_type']]
        similar_countries = same_cluster.nsmallest(6, 'volatility_std')['country'].tolist()
        
        if selected_country in similar_countries:
            similar_countries.remove(selected_country)
        
        st.write(f"Countries with similar stability patterns: {', '.join(similar_countries[:5])}")

def show_raw_data(df):
    """Raw data explorer"""
    
    st.header("📋 Raw Data Explorer")
    
    # Data preview
    st.subheader("Dataset Preview")
    
    columns_to_show = st.multiselect(
        "Select columns to display:",
        df.columns.tolist(),
        default=['country', 'cluster_type', 'volatility_std', 'extreme_positive_count', 'stability_inverse_volatility']
    )
    
    if columns_to_show:
        st.dataframe(df[columns_to_show], use_container_width=True, height=400)
    
    # Data statistics
    st.subheader("Dataset Statistics")
    st.write(df.describe())
    
    # Download options
    st.subheader("📥 Download Data")
    
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download Full Dataset as CSV",
        data=csv,
        file_name="food_price_stability_clusters.csv",
        mime="text/csv"
    )

if __name__ == "__main__":
    main()