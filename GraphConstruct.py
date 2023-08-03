def construct_graph(text, similarity_threshold):
    text = text.lower()
    sentences = sent_tokenize(text)
    similarity_matrix = cosine_similarity(sentences)
    graph = nx.Graph()
    graph.add_nodes_from(range(len(sentences)))
    for i in range(len(sentences)):
        for j in range(i + 1, len(sentences)):
            similarity = similarity_matrix[i][j]
            if similarity > similarity_threshold:
                graph.add_edge(i, j, weight=similarity)
    return graph
