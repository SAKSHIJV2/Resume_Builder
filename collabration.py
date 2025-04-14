from graphviz import Digraph

def create_collaboration_diagram():
    dot = Digraph('Collaboration Diagram', filename='collaboration_diagram', format='png')
    
    # Nodes for key participants
    dot.node('U', 'User (Applicant)', shape='box')
    dot.node('S', 'AI Resume Builder System', shape='box')
    dot.node('D', 'Database', shape='box')
    dot.node('AI', 'AI Service', shape='box')
    
    # Interactions between entities
    dot.edge('U', 'S', label='1: Select Template')
    dot.edge('S', 'D', label='2: Fetch Templates')
    dot.edge('D', 'S', label='3: Return Templates')
    dot.edge('S', 'U', label='4: Display Templates')
    dot.edge('U', 'S', label='5: Enter Resume Details')
    dot.edge('S', 'AI', label='6: Check Grammar & Suggestions')
    dot.edge('AI', 'S', label='7: Return AI Suggestions')
    dot.edge('S', 'U', label='8: Display Corrections')
    dot.edge('U', 'S', label='9: Finalize Resume')
    dot.edge('S', 'D', label='10: Store Resume Data')
    dot.edge('S', 'U', label='11: Provide Download Options')
    dot.edge('U', 'S', label='12: Download Resume')
    
    # Diagram structure
    dot.attr(rankdir='BT')  # Bottom-to-top flow for better readability
    
    dot.render()
    
create_collaboration_diagram()
