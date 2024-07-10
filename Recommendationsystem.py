#import numpy as np


ratings = np.array([
    [5, 3, 0, 2, 5, 1],  # User 1
    [2, 0, 4, 1, 0, 3],  # User 2
    [1, 4, 5, 2, 4, 0],  # User 3
    [4, 0, 0, 3, 2, 5],  # User 4
    [0, 2, 3, 0, 1, 4],  # User 5
    [3, 0, 4, 0, 0, 2]   # User 6
])


def cosine_similarity(user1, user2):
    mask = np.logical_and(user1 != 0, user2 != 0)  
    if np.any(mask):
        # Compute cosine similarity
        numerator = np.sum(user1[mask] * user2[mask])
        denominator = np.sqrt(np.sum(user1[mask] ** 2)) * np.sqrt(np.sum(user2[mask] ** 2))
        return numerator / denominator
    else:
        return 0.0

def recommend_items(user_id, ratings_matrix, num_recommendations=5):
    similarities = []
    for i in range(ratings_matrix.shape[0]):
        if i != user_id:
            similarity = cosine_similarity(ratings_matrix[user_id], ratings_matrix[i])
            similarities.append((i, similarity))
    
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    top_similar_users = similarities[:num_recommendations]
    
    recommendations = []
    target_user_ratings = ratings_matrix[user_id]
    for user, similarity in top_similar_users:
        similar_user_ratings = ratings_matrix[user]
        for i in range(len(similar_user_ratings)):
            if target_user_ratings[i] == 0 and similar_user_ratings[i] != 0:
                recommendations.append((i, similar_user_ratings[i]))
    
    recommendations.sort(key=lambda x: x[1], reverse=True)

    top_recommendations = [movie_id for movie_id, rating in recommendations[:num_recommendations]]
    
    return top_recommendations

user_id = 0  # User for whom we want to recommend items (index starts from 0)
recommended_items = recommend_items(user_id, ratings)

print(f"Recommended items for User {user_id + 1}:")
for item_id in recommended_items:
    print(f"Item {item_id + 1}")
