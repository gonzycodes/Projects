def apply_spell(caster,target,spell):
    amount = spell.cast()

    if spell.spell_type == "damage":
        target.adjust_health(-amount)
        return f"{caster.name} used {spell.name} and dealt {amount} damage!"
    
    elif spell.spell_type == "heal":
        caster.adjust_health(amount)
        return f"{caster.name} used {spell.name} and restored {amount}hp "