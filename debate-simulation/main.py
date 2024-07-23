from src.agents.debate_agent import DebateAgent
from src.agents.moderator import Moderator
from src.agents.judge_agent import JudgeAgent
from src.agents.audience_member import AudienceMember
from src.agents.scoring_agent import ScoringAgent

def run_audience_vote(debate_history, num_voters=10):
    votes = {"Debater1": 0, "Debater2": 0}
    for _ in range(num_voters):
        voter = AudienceMember()
        vote = voter.vote(debate_history).strip()
        if vote in votes:
            votes[vote] += 1
    
    winner = max(votes, key=votes.get)
    return winner, votes

def run_debate(topic, rounds=2):
    debater1 = DebateAgent("Debater1", "In favor of the topic")
    debater2 = DebateAgent("Debater2", "Against the topic")
    moderator = Moderator()
    judge = JudgeAgent()
    scorer = ScoringAgent()
    
    debate_history = f"Topic: {topic}\n\n"
    scores = {"Debater1": 0, "Debater2": 0}
    
    for i in range(rounds):
        print(f"Round {i+1}")
        
        # Moderator introduces the round
        mod_input = f"Introduce round {i+1} of the debate on {topic}"
        mod_response = moderator.moderate(debate_history, mod_input)
        debate_history += f"Moderator: {mod_response}\n\n"
        print(f"Moderator: {mod_response}")
        
        # Debater 1's turn
        debater1_response = debater1.respond(topic)
        debate_history += f"Debater1: {debater1_response}\n\n"
        print(f"Debater1: {debater1_response}")
        
        # Debater 2's turn
        debater2_response = debater2.respond(debater1_response)
        debate_history += f"Debater2: {debater2_response}\n\n"
        print(f"Debater2: {debater2_response}")
        
        # Score the round
        round_content = f"Debater1: {debater1_response}\nDebater2: {debater2_response}"
        round_scores = scorer.score_round(round_content)
        print(f"Round Scores:\n{round_scores}")
        for line in round_scores.split("\n"):
            if ":" in line:
                debater, score_str = line.split(":")
                debater = debater.strip()
                score_str = score_str.strip()
                try:
                    score = int(score_str.strip("[]"))
                    scores[debater] += score
                except ValueError:
                    print(f"Warning: Invalid score format for {debater}: {score_str}")
        
        print("\n")
    
    # Moderator concludes the debate
    mod_input = f"Conclude the debate on {topic}"
    mod_response = moderator.moderate(debate_history, mod_input)
    debate_history += f"Moderator: {mod_response}\n\n"
    print(f"Moderator: {mod_response}")
    
    # Judge's decision
    judge_decision = judge.judge_debate(debate_history)
    print(f"Judge's Decision:\n{judge_decision}")
    
    # Audience vote
    audience_winner, vote_counts = run_audience_vote(debate_history)
    print(f"Audience Vote Results: {vote_counts}")
    print(f"Audience Winner: {audience_winner}")
    
    # Scoring system winner
    scoring_winner = max(scores, key=scores.get)
    print(f"Final Scores: {scores}")
    print(f"Scoring System Winner: {scoring_winner}")

if __name__ == "__main__":
    run_debate("Is leaving the city a good idea?")