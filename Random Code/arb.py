def calculate_implied_probability(decimal_odds):
    return 1 / decimal_odds

def find_arbitrage_opportunity(odds_list):
    total_implied_prob = sum(calculate_implied_probability(odds) for odds in odds_list)

    if total_implied_prob < 1.0:
        print("Arbitrage opportunity detected!")
        bet_amount = 100  # Total investment (adjust as needed)

        for i, odds in enumerate(odds_list):
            implied_prob = calculate_implied_probability(odds)
            bet_on_team = f"Team {i + 1}"
            bet_amount_team = bet_amount * implied_prob / total_implied_prob
            print(f"Bet ${bet_amount_team:.2f} on {bet_on_team} (Odds: {odds:.2f})")
    else:
        print("No arbitrage opportunity.")

if __name__ == "__main__":
    # Example odds (replace with real data)
    odds_site1 = 2.10
    odds_site2 = 1.90
    odds_site3 = 2.05
    # ... add more odds for other sites ...

    odds_list = [odds_site1, odds_site2, odds_site3]  # Add all 10 odds here
    find_arbitrage_opportunity(odds_list)
