BEGIN;

-- Seed abilities
INSERT INTO ability (name, effect_entries) VALUES
('overgrow', $$[{"effect":"When this Pokémon has 1/3 or less of its HP remaining, its grass-type moves inflict 1.5× as much regular damage.","short_effect":"Strengthens grass moves to inflict 1.5× damage at 1/3 max HP or less.","language":{"name":"en"}}]$$::json),
('blaze', $$[{"effect":"When this Pokémon has 1/3 or less of its HP remaining, its fire-type moves inflict 1.5× as much regular damage.","short_effect":"Strengthens fire moves to inflict 1.5× damage at 1/3 max HP or less.","language":{"name":"en"}}]$$::json),
('torrent', $$[{"effect":"When this Pokémon has 1/3 or less of its HP remaining, its water-type moves inflict 1.5× as much regular damage.","short_effect":"Strengthens water moves to inflict 1.5× damage at 1/3 max HP or less.","language":{"name":"en"}}]$$::json),
('chlorophyll', $$[{"effect":"This Pokémon's Speed is doubled during strong sunlight.","short_effect":"Doubles Speed during strong sunlight.","language":{"name":"en"}}]$$::json),
('static', $$[{"effect":"This Pokémon's body is composed of static electricity, so contact with it may cause paralysis.","short_effect":"Has a 30% chance of paralyzing attacking Pokémon on contact.","language":{"name":"en"}}]$$::json),
('adaptability', $$[{"effect":"This Pokémon's STAB modifier is 2 instead of 1.5.","short_effect":"Increases the same-type attack bonus from 1.5× to 2×.","language":{"name":"en"}}]$$::json),
('run-away', $$[{"effect":"This Pokémon is always successful fleeing from wild battles, even if trapped by moves or abilities.","short_effect":"Ensures success fleeing from wild battles.","language":{"name":"en"}}]$$::json),
('immunity', $$[{"effect":"This Pokémon cannot be poisoned. If already poisoned, it will cure itself upon switching in.","short_effect":"Prevents poisoning.","language":{"name":"en"}}]$$::json),
('thick-fat', $$[{"effect":"This Pokémon takes half damage from Fire- and Ice-type moves.","short_effect":"Halves damage from Fire and Ice moves.","language":{"name":"en"}}]$$::json),
('pressure', $$[{"effect":"This Pokémon's moves have their PP deducted twice as fast.","short_effect":"Doubles the PP cost of moves used against this Pokémon.","language":{"name":"en"}}]$$::json),
('inner-focus', $$[{"effect":"This Pokémon will not flinch. Moves that would normally cause flinching will not work.","short_effect":"Prevents flinching.","language":{"name":"en"}}]$$::json),
('intimidate', $$[{"effect":"When this Pokémon enters battle, the opponent's Attack is lowered by one stage.","short_effect":"Lowers the foe's Attack stat.","language":{"name":"en"}}]$$::json),
('water-absorb', $$[{"effect":"This Pokémon heals 1/4 of its maximum HP when hit by a Water-type move.","short_effect":"Heals 25% HP when hit by Water moves.","language":{"name":"en"}}]$$::json),
('shell-armor', $$[{"effect":"This Pokémon cannot be struck by a critical hit.","short_effect":"Protects against critical hits.","language":{"name":"en"}}]$$::json),
('synchronize', $$[{"effect":"If this Pokémon is poisoned, badly poisoned, paralyzed, or burned, the opponent will be afflicted with the same status condition.","short_effect":"Passes on status conditions to the opponent.","language":{"name":"en"}}]$$::json),
('steadfast', $$[{"effect":"This Pokémon's Speed rises by one stage every time it flinches.","short_effect":"Raises Speed each time the Pokémon flinches.","language":{"name":"en"}}]$$::json),
('sand-veil', $$[{"effect":"This Pokémon's evasion is increased by 20% in a sandstorm.","short_effect":"Ups evasion in a sandstorm.","language":{"name":"en"}}]$$::json),
('clear-body', $$[{"effect":"This Pokémon's stats cannot be lowered by other Pokémon's moves or abilities.","short_effect":"Prevents stat reduction.","language":{"name":"en"}}]$$::json),
('trace', $$[{"effect":"When this Pokémon enters battle, it copies the opponent's ability.","short_effect":"Copies the foe's ability.","language":{"name":"en"}}]$$::json),
('truant', $$[{"effect":"This Pokémon can only use a move every other turn.","short_effect":"Moves only every two turns.","language":{"name":"en"}}]$$::json),
('sand-stream', $$[{"effect":"The Pokémon summons a sandstorm when it enters a battle.","short_effect":"Summons a sandstorm.","language":{"name":"en"}}]$$::json),
('swift-swim', $$[{"effect":"This Pokémon's Speed is doubled during rain.","short_effect":"Doubles Speed in rain.","language":{"name":"en"}}]$$::json),
('sniper', $$[{"effect":"This Pokémon's critical hits deal 3× damage instead of 2×.","short_effect":"Boosts critical hit damage.","language":{"name":"en"}}]$$::json),
('marvel-scale', $$[{"effect":"This Pokémon's Defense is increased by 50% when it is affected by a status condition.","short_effect":"Ups Defense if suffering a status condition.","language":{"name":"en"}}]$$::json),
('competitive', $$[{"effect":"This Pokémon's Special Attack rises by two stages when one of its stats is lowered.","short_effect":"Sharply raises Special Attack when a stat is lowered.","language":{"name":"en"}}]$$::json)
ON CONFLICT (name) DO NOTHING;

-- Seed pokemon
INSERT INTO pokemon (name) VALUES
('bulbasaur'),
('charmander'),
('squirtle'),
('venusaur'),
('pikachu'),
('charizard'),
('blastoise'),
('eevee'),
('snorlax'),
('mewtwo'),
('dragonite'),
('gyarados'),
('lapras'),
('mew'),
('lucario'),
('garchomp'),
('salamence'),
('metagross'),
('gallade'),
('gardevoir'),
('slaking'),
('tyranitar'),
('kingdra'),
('milotic')
ON CONFLICT (name) DO NOTHING;

-- Seed pokemon_ability associations
INSERT INTO pokemon_ability (pokemon_id, ability_id)
SELECT p.id, a.id FROM pokemon p, ability a
WHERE (p.name, a.name) IN (
    ('bulbasaur', 'overgrow'),
    ('bulbasaur', 'chlorophyll'),
    ('charmander', 'blaze'),
    ('squirtle', 'torrent'),
    ('venusaur', 'overgrow'),
    ('venusaur', 'chlorophyll'),
    ('pikachu', 'static'),
    ('charizard', 'blaze'),
    ('blastoise', 'torrent'),
    ('eevee', 'adaptability'),
    ('eevee', 'run-away'),
    ('snorlax', 'immunity'),
    ('snorlax', 'thick-fat'),
    ('mewtwo', 'pressure'),
    ('dragonite', 'inner-focus'),
    ('gyarados', 'intimidate'),
    ('lapras', 'water-absorb'),
    ('lapras', 'shell-armor'),
    ('mew', 'synchronize'),
    ('lucario', 'steadfast'),
    ('lucario', 'inner-focus'),
    ('garchomp', 'sand-veil'),
    ('salamence', 'intimidate'),
    ('metagross', 'clear-body'),
    ('gallade', 'steadfast'),
    ('gardevoir', 'synchronize'),
    ('gardevoir', 'trace'),
    ('slaking', 'truant'),
    ('tyranitar', 'sand-stream'),
    ('kingdra', 'swift-swim'),
    ('kingdra', 'sniper'),
    ('milotic', 'marvel-scale'),
    ('milotic', 'competitive')
)
ON CONFLICT (pokemon_id, ability_id) DO NOTHING;

COMMIT;
