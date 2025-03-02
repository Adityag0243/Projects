
import matplotlib.pyplot as plt

def plotGraph(no_of_hash, false_positives, sz, multiplier):
    plt.figure(figsize=(8, 5))
    hash_function_range = list(range(2, no_of_hash + 1))
    plt.plot(hash_function_range, false_positives, marker='o', linestyle='-', color='b', label="False Positive %");
    # Formatting

    plt.xlabel("Number of Hash Functions Used")
    plt.ylabel("False Positive Rate")
   
    plt.title(f"False Positive % vs. No. of Hash Functions")
    plt.text(
        0.5, 0.1,  # Adjust position inside the graph
        f"Size of IPs: {sz}\nMultiplier: {multiplier}",
        transform=plt.gca().transAxes,
        fontsize=10, bbox=dict(facecolor='white', alpha=0.5)
    )

    # Find the minimum false positive rate and its corresponding hash function count
    min_fp = min(false_positives)
    min_fp_index = false_positives.index(min_fp)
    min_hash_function = hash_function_range[min_fp_index]

    plt.annotate(f'Min_false_pos: {min_fp:.2f}% \nHash: {min_hash_function}', 
             xy=(min_hash_function, min_fp), 
             xytext=(min_hash_function + 1, min_fp + 0.01),  # Adjust text position
             arrowprops=dict(facecolor='red', shrink=0.05),
             fontsize=10, color='red',
             bbox=dict(facecolor='lightgrey', edgecolor='black', boxstyle='round,pad=0.3'))  # Light grey background
    
    
    plt.legend()
    plt.grid()
    plt.show()
