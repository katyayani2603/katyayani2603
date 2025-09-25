
import pandas as pd

# Read both files
df_transcript = pd.read_csv('Inspira_250_HnB_Batch1_v2 2.csv')
df_clusters = pd.read_csv('tcx-intent-clusters_CXJ-005D_2025-09-25 3.csv')

# Map Transcripts from df_transcript to df_clusters using transcriptID
df_clusters = df_clusters.merge(
    df_transcript[['transcriptID', 'Transcripts']],
    left_on='transcriptId',
    right_on='transcriptID',
    how='left'
)

# Save the new file
df_clusters.to_csv('clusters_with_transcripts.csv', index=False)

# --- Add this code after your existing code ---

# Read tcx-intents file
df_intents = pd.read_csv('tcx-intents_CXJ-005D_2025-09-25 3.csv')

# Map Transcripts from df_transcript to df_intents using transcriptId
df_intents = df_intents.merge(
    df_transcript[['transcriptID', 'Transcripts']],
    left_on='transcriptId',
    right_on='transcriptID',
    how='left'
)

# Save the new file
df_intents.to_csv('tcx_intents_with_transcripts.csv', index=False)
