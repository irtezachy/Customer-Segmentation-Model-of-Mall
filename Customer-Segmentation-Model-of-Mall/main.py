import pickle
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from src.data.make_dataset import load_data
from src.models.train_model import train_k_means
from src.visualization.visualize import pairplot,elbow_plot, silhouette_plot, show_clusters
# Load and preprocess the data
data_Source = "Customer-Segmentation-Model-of-Mall\\data\\raw\\mall_customers.csv"
df = load_data(data_Source)

print("Pairplot for viewing corelations and finding clear patterns:")
pairplot(df,"Customer-Segmentation-Model-of-Mall\\reports\\figures\\pairplot.png")
    
#Train the K-means model
kmodel, wss = train_k_means(df[['Annual_Income','Spending_Score']])
    
# Save the trained model
with open('Customer-Segmentation-Model-of-Mall\\models\\k_means_with_Annual_Income_And_Spending_Score.pkl', 'wb') as f:
    pickle.dump(kmodel, f)

print("Save Elbow plot:")
elbow_plot(wss,"Customer-Segmentation-Model-of-Mall\\reports\\figures\\Elbow_Plot1.png")
    
print("Save Silhouette plot:")
silhouette_plot(wss,"Customer-Segmentation-Model-of-Mall\\reports\\figures\\Silhouette_Plot1.png")

print("Cluster centers:")
for k, center in enumerate(kmodel.cluster_centers_, start=1):
    print(f"Cluster: {k}  Center: {center}")    
       
df['Clusters_2_Features'] = kmodel.labels_
    
show_clusters(df,'Clusters_2_Features','Customer-Segmentation-Model-of-Mall\\reports\\figures\\Clusters_with_2_features.png')
    
print("K-Means using all available features:")
#Train the K-means model
kmodel, wss = train_k_means(df[['Age','Annual_Income','Spending_Score']])
    
# Save the trained model
with open('Customer-Segmentation-Model-of-Mall\\models\\modelsk_means_with_All_Features.pkl', 'wb') as f:
    pickle.dump(kmodel, f)

print("Save Elbow plot:")
elbow_plot(wss,"Customer-Segmentation-Model-of-Mall\\reports\\figures\\Elbow_Plot2.png")
    
print("Save Silhouette plot:")
elbow_plot(wss,"Customer-Segmentation-Model-of-Mall\\reports\\figures\\Silhouette_Plot2.png")

print("Cluster centers:")
for k, center in enumerate(kmodel.cluster_centers_, start=1):
    print(f"Cluster: {k}  Center: {center}")

df['Clusters_all_features'] = kmodel.labels_
    
show_clusters(df,'Clusters_2_Features','Customer-Segmentation-Model-of-Mall\\reports\\figures\\Clusters_with_all_features.png')