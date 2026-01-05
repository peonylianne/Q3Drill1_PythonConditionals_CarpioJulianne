from pyscript import document

def compute_average(event):
    score1 = float(document.getElementById("score1").value)
    score2 = float(document.getElementById("score2").value)

    # Compute Average
    average = (score1 + score2) / 2

    # Determine Pass/Fail
    if average >= 75:
        result = "Yes"
    else:
        result = "No"

    # Display results
    document.getElementById("average").innerText = str(round(average, 2))
    document.getElementById("result").innerText = result
