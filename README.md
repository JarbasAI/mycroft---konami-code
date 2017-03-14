# mycroft---konami-code

upon sequential entry of konami code execute user script

# usage

    up
    up
    ->register down intent
    down
    down
    -> register left
    left 
    -> register right
    right
    -> register left
    left 
    -> register b
    b
    -> register a
    a
    -> speak cheat code unlocked
    -> execute cheat_code.py
    
 bad sequence resets input (require converse method)
    

# requires

[De-register Intents PR#553](https://github.com/MycroftAI/mycroft-core/issues/553)

[Converse Method PR#539](https://github.com/MycroftAI/mycroft-core/pull/539)
