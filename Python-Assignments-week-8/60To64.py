# Assignment One
def get_score(**materials):
    for material_key, material_value in materials.items():
        print(f"{material_key} => {material_value}")


get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)


##########################################################

# Assignment Two
def get_people_scores(name="", **subjects):
    if name == "":
        for subject_key, subject_value in subjects.items():
            print(f"{subject_key} => {subject_value}")
    else:
        print(f"Hello {name} This is Your Score Table: ")
        for subject_key, subject_value in subjects.items():
            print(f"{subject_key} => {subject_value}")
    if subjects == {}:
        print(f"Hello {name} You Have No Scores To Show")


# Test 1
get_people_scores("Osama", Math=90, Science=80, Language=70)

# Output
"Hello Osama This Is Your Score Table:"
"Math => 90"
"Science => 80"
"Language => 70"

# Test 2
get_people_scores("Mahmoud", Logic=70, Problems=60)

# Output
"Hello Mahmoud This Is Your Score Table:"
"Logic => 70"
"Problems => 60"

# Test 3
get_people_scores(Logic=70, Problems=60)

# Output
"Logic => 70"
"Problems => 60"

# Test 4
get_people_scores("Ahmed")

# Output
"Hello Ahmed You Have No Scores To Show"

################################################################

# Assignment Three
scores_list = {
    "Math": "90",
    "Science": "80",
    "Language": "70"
}


def get_the_scores(name="", **scores):
    if name == "":
        for score_key, score_value in scores.items():
            print(f"{score_key} => {score_value}")
    elif name != "" and scores != {}:
        print(f"Hello {name} This Is Your Score Table:")
        for score_key, score_value in scores.items():
            print(f"{score_key} => {score_value}")
    if scores == {}:
        print(f"Hello {name} You Have No Scores To Show")


get_the_scores(**scores_list)
