def simple_chatbot(user_query):
    # Standardize user query to handle accidental spaces or capitalization
    query = user_query.strip().lower()
    
    if "what is the total revenue of microsoft in 2024" in query:
        return "The total revenue of Microsoft in 2024 is $245,122 million."
        
    elif "how has net income changed for tesla over the last year" in query:
        return "The net income for Tesla has decreased by -45.64% from 2024 to 2025."
        
    elif "compare revenue growth in 2025" in query:
        return ("In 2025, Year-over-Year Revenue Growth was:\n"
                "- Microsoft: 14.93%\n"
                "- Apple: 6.43%\n"
                "- Tesla: -2.93%")
                
    elif "what are apple's total assets in 2024" in query:
        return "Apple's Total Assets in 2024 stood at $364,980 million."
        
    else:
        return "Sorry, I can only provide information on predefined queries."

# Quick test execution to verify functionality
print("Bot Response 1:", simple_chatbot("What is the total revenue of Microsoft in 2024?"))
print("Bot Response 2:", simple_chatbot("How has net income changed for Tesla over the last year?"))