# Specificity: Range how clearly the goals of the project are defined with clear objectives, making it easier to understand.
# Relevence: Range where it shows how closely the project aligns with the target population. 
# Effectiveness: Range if the strategies and approaches are correct.

def get_user_input():
    name = input("Project Name: ")
    print("Range 0 - 10")
    specificity = float(input("Specificity score: "))
    relevance = float(input("Relevance score: "))
    effectiveness = float(input("Effectiveness score: "))
    
    return {'name': name, 'specificity': specificity, 'relevance': relevance, 'effectiveness': effectiveness}

#Used normalization here to get the range between 0 and 1 Formula : value / max_value
def calculate_normalized_score(value, max_value):
    return value / max_value if max_value != 0 else 0

def calculate_total_score(project, weights):
    normalized_specificity = calculate_normalized_score(project['specificity'], 10)
    normalized_relevance = calculate_normalized_score(project['relevance'], 10)
    normalized_effectiveness = calculate_normalized_score(project['effectiveness'], 10)

    weighted_specificity = normalized_specificity * weights['specificity']
    weighted_relevance = normalized_relevance * weights['relevance']
    weighted_effectiveness = normalized_effectiveness * weights['effectiveness']

    return weighted_specificity + weighted_relevance + weighted_effectiveness

def rank_projects(projects, weights, cutoff):
    ranked_projects = []

    for project in projects:
        total_score = calculate_total_score(project, weights)

        if total_score >= cutoff:
            ranked_projects.append({'project': project, 'score': total_score})

    ranked_projects.sort(key=lambda x: x['score'], reverse=True)
    return ranked_projects

def main():
    projects = []
    weights = {'specificity': 0.3, 'relevance': 0.4, 'effectiveness': 0.3}
    cutoff = 0.6  #Cutoff can be adjusted based on the needs

    # Add projects
    num_projects = int(input("Enter the number of projects: "))
    for _ in range(num_projects):
        projects.append(get_user_input())

    # Ranks of the projects
    result = rank_projects(projects, weights, cutoff)

    # Results
    if result:
        print("\nRanked Projects:")
        for idx, entry in enumerate(result, start=1):
            formatted_score = '{:.2f}'.format(entry['score'])
            print(f"{idx}. {entry['project']['name']} - Score: {formatted_score}")
    else:
        print("\nNo projects meet the cutoff criteria.")
    
    print("\nProjects not meeting the cutoff:")
    for project in projects:
        total_score = calculate_total_score(project, weights)
        formatted_score = '{:.2f}'.format(entry['score'])

        if total_score < cutoff:
            print(f"{project['name']} - Score: {formatted_score}")

if __name__ == "__main__":
    main()
