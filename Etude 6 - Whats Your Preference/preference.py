votes = []  # array of all votes
candidates = set()  # set of candidate names
round = 1  # current round
rounds = {}  # stores a version of vote counts from each round


def tiebreak(tied, current_round):
    if len(tied) == 1:
        return tied[0]

    # iterate in reverse order from current round to first round
    for i in reversed(range(1, current_round)):
        previous_round = rounds[i]  # get a copy of the previous round vote count
        previous_round = [
            i for i in previous_round if i[0] in tied
        ]  # remove non-tiebreak contenders from vote count

        # Add all tiebreakers of this previous round to array
        lowest = previous_round[len(previous_round) - 1][1]
        tied = []
        for j in reversed(previous_round):
            if j[1] == lowest:
                tied.append(j[0])
            else:
                break

        # Recurse
        return tiebreak(tied, i)

    # Return none if unbreakable tie
    return


# Eliminates a candidate from votes
def eliminate(votes):
    vote_count = count_votes(votes)  # get vote count array of current votes
    rounds[round] = vote_count  # store a version of vote count for current round

    lowest = vote_count[len(vote_count) - 1][1]  # value of lowest vote count
    tied = []  # array of candidates with the lowest vote count
    for i in reversed(vote_count):
        if i[1] == lowest:
            tied.append(i[0])
        else:
            break

    last = tiebreak(tied, round)  # get player to eliminate
    if not last:  # if unbreakable tie
        return vote_count, last
    candidates.remove(last)  # remove last player from set of candidates

    # If there is 1 candidate remaining
    if len(candidates) == 1:
        vote_count = [i for i in vote_count if i[0] is not last]
        return vote_count, last

    # Remove last player from array of all votest
    for voter in votes:
        voter[:] = [i for i in voter if i != last]
        
    votes[:] = [i for i in votes if i != []]

    vote_count = count_votes(votes)
    return vote_count, last


# Counts the number of votes for each candidate given an array of all votes
def count_votes(votes):
    vote_count = {}  # dictionary of candidates and vote counts

    # Add candidate to vote_count dictionary
    for candidate in candidates:
        vote_count[candidate] = 0

    # print(vote_count)
    # Update dictionary values for each candidate
    for voter in votes:
        vote_count[voter[0]] += 1

    # Convert dictionary of vote counts to an array
    vote_count = sorted(
        vote_count.items(), key=lambda x: x[0]
    )  # sort by alphabetical order of candidate
    vote_count = sorted(
        vote_count, key=lambda x: x[1], reverse=True
    )  # sort by number of votes

    return vote_count


def print_votes(votes):
    vote_count = count_votes(votes)
    print("Round " + str(round))

    longest = max(len(name) for name, x in vote_count)
    for name, count in vote_count:
        print(f"{name:{longest}}   {count}")

    total_votes = sum(candidate[1] for candidate in vote_count)
    # If a candidate has more than half the votes
    if vote_count[0][1] > total_votes / 2:
        print("Winner: " + vote_count[0][0])
        exit()

    vote_count, eliminated = eliminate(votes)
    if not eliminated:
        print("Unbreakable tie")
        exit()
    else:
        print("Eliminated: " + eliminated)
    print("\n")


if __name__ == "__main__":
    # Get votes from input and place in array of votes
    while True:
        try:
            voter = input()
        except EOFError:
            break

        # if not voter.strip():
        #     continue

        voter = voter.split(" ")
        voter = [i for i in voter if i != ""]
        votes.append(voter)

    # Add to set of candidates
    for voter in votes:
        for vote in voter:
            if vote not in candidates:
                candidates.add(vote)

    # While there are over two candidates left
    while len(candidates) > 2:
        print_votes(votes)
        round += 1

    # Last round
    vote_count = count_votes(votes)
    print("Round " + str(round))
    longest = max(len(name) for name, x in vote_count)
    for name, count in vote_count:
        print(f"{name:{longest}}   {count}")
    vote_count, eliminated = eliminate(votes)
    if not eliminated:
        print("Unbreakable tie")
    else:
        print("Winner: " + vote_count[0][0])
