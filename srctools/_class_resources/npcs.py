"""NPC entities."""
from srctools._class_resources import *


@cls_func
def npc_antlion(pack: PackList, ent: Entity):
    """Antlions require different resources for the worker version."""
    spawnflags = conv_int(ent['spawnflags'])
    if spawnflags & (1 << 18):  # Is worker?
        pack.pack_file("models/antlion_worker.mdl", FileType.MODEL)
        pack.pack_file("blood_impact_antlion_worker_01", FileType.PARTICLE)
        pack.pack_file("antlion_gib_02", FileType.PARTICLE)
        pack.pack_file("blood_impact_yellow_01", FileType.PARTICLE)

        for fname, ftype in CLASS_RESOURCES['grenade_spit']:
            pack.pack_file(fname, ftype)
    else:
        pack.pack_file("models/antlion.mdl", FileType.MODEL)
        pack.pack_file("blood_impact_antlion_01")
        pack.pack_file("AntlionGib", FileType.PARTICLE)

    for i in ('1', '2', '3'):
        for size in ('small', 'medium', 'large'):
            pack.pack_file("models/gibs/antlion_gib_{}_{}.mdl".format(size, i), FileType.MODEL)

    pack.pack_soundscript("NPC_Antlion.RunOverByVehicle")
    pack.pack_soundscript("NPC_Antlion.MeleeAttack")
    pack.pack_soundscript("NPC_Antlion.Footstep")
    pack.pack_soundscript("NPC_Antlion.BurrowIn")
    pack.pack_soundscript("NPC_Antlion.BurrowOut")
    pack.pack_soundscript("NPC_Antlion.FootstepSoft")
    pack.pack_soundscript("NPC_Antlion.FootstepHeavy")
    pack.pack_soundscript("NPC_Antlion.MeleeAttackSingle")
    pack.pack_soundscript("NPC_Antlion.MeleeAttackDouble")
    pack.pack_soundscript("NPC_Antlion.Distracted")
    pack.pack_soundscript("NPC_Antlion.Idle")
    pack.pack_soundscript("NPC_Antlion.Pain")
    pack.pack_soundscript("NPC_Antlion.Land")
    pack.pack_soundscript("NPC_Antlion.WingsOpen")
    pack.pack_soundscript("NPC_Antlion.LoopingAgitated")
    pack.pack_soundscript("NPC_Antlion.Distracted")

    # TODO: These are Episodic only..
    pack.pack_soundscript("NPC_Antlion.PoisonBurstScream")
    pack.pack_soundscript("NPC_Antlion.PoisonBurstScreamSubmerged")
    pack.pack_soundscript("NPC_Antlion.PoisonBurstExplode")
    pack.pack_soundscript("NPC_Antlion.MeleeAttack_Muffled")
    pack.pack_soundscript("NPC_Antlion.TrappedMetal")
    pack.pack_soundscript("NPC_Antlion.ZappedFlip")
    pack.pack_soundscript("NPC_Antlion.PoisonShoot")
    pack.pack_soundscript("NPC_Antlion.PoisonBall")

res('npc_antlion_grub',
    mdl("models/antlion_grub.mdl"),
    mdl("models/antlion_grub_squashed.mdl"),
    mat("materials/sprites/grubflare1.vmt"),
    sound("NPC_Antlion_Grub.Idle"),
    sound("NPC_Antlion_Grub.Alert"),
    sound("NPC_Antlion_Grub.Stimulated"),
    sound("NPC_Antlion_Grub.Die"),
    sound("NPC_Antlion_Grub.Squish"),
    part("GrubSquashBlood"),
    part("GrubBlood"),
    includes="item_grubnugget",
    )


@cls_func
def npc_antlion_template_maker(pack: PackList, ent: Entity):
    """Depending on KVs this may or may not spawn workers."""
    # There will be an antlion present in the map, as the template
    # NPC. So we don't need to add those resources.
    if conv_int(ent['workerspawnrate']) > 0:
        # It randomly spawns worker antlions, so load that resource set.
        pack.pack_file("models/antlion_worker.mdl", FileType.MODEL)
        pack.pack_file("blood_impact_antlion_worker_01", FileType.PARTICLE)
        pack.pack_file("antlion_gib_02", FileType.PARTICLE)
        pack.pack_file("blood_impact_yellow_01", FileType.PARTICLE)

        for fname, ftype in CLASS_RESOURCES['grenade_spit']:
            pack.pack_file(fname, ftype)

res('npc_barnacle',
    mdl('models/barnacle.mdl'),
    mdl("models/gibs/hgibs.mdl"),
    mdl("models/gibs/hgibs_scapula.mdl"),
    mdl("models/gibs/hgibs_rib.mdl"),
    mdl("models/gibs/hgibs_spine.mdl"),
    sound("NPC_Barnacle.Digest"),
    sound("NPC_Barnacle.BreakNeck"),
    sound("NPC_Barnacle.Scream"),
    sound("NPC_Barnacle.PullPant"),
    sound("NPC_Barnacle.TongueStretch"),
    sound("NPC_Barnacle.FinalBite"),
    sound("NPC_Barnacle.Die"),
    includes='npc_barnacle_tongue_tip',
    )
res('npc_barnacle_tongue_tip', 'models/props_junk/rock001a.mdl')  # Random model it loads.
res('npc_cscanner',
    # In HL2, the claw scanner variant is chosen if the map starts with d3_c17.
    # In episodic, npc_clawscanner is now available to force that specifically.
    # TODO: Check the BSP name, pack shield in that case.
    mdl("models/combine_scanner.mdl"),
    mdl("models/gibs/scanner_gib01.mdl"),
    mdl("models/gibs/scanner_gib02.mdl"),
    mdl("models/gibs/scanner_gib02.mdl"),
    mdl("models/gibs/scanner_gib04.mdl"),
    mdl("models/gibs/scanner_gib05.mdl"),
    mat("material/sprites/light_glow03.vmt"),
    sound("NPC_CScanner.Shoot"),
    sound("NPC_CScanner.Alert"),
    sound("NPC_CScanner.Die"),
    sound("NPC_CScanner.Combat"),
    sound("NPC_CScanner.Idle"),
    sound("NPC_CScanner.Pain"),
    sound("NPC_CScanner.TakePhoto"),
    sound("NPC_CScanner.AttackFlash"),
    sound("NPC_CScanner.DiveBombFlyby"),
    sound("NPC_CScanner.DiveBomb"),
    sound("NPC_CScanner.DeployMine"),
    sound("NPC_CScanner.FlyLoop"),
    )
res('npc_combine_cannon',
    mdl('models/combine_soldier.mdl'),
    mat('materials/effects/bluelaser1.vmt'),
    mat('materials/sprites/light_glow03.vmt'),
    sound('NPC_Combine_Cannon.FireBullet'),
    )
res('npc_clawscanner',
    mdl("models/shield_scanner.mdl"),
    mdl("models/gibs/Shield_Scanner_Gib1.mdl"),
    mdl("models/gibs/Shield_Scanner_Gib2.mdl"),
    mdl("models/gibs/Shield_Scanner_Gib3.mdl"),
    mdl("models/gibs/Shield_Scanner_Gib4.mdl"),
    mdl("models/gibs/Shield_Scanner_Gib5.mdl"),
    mdl("models/gibs/Shield_Scanner_Gib6.mdl"),
    mat("material/sprites/light_glow03.vmt"),

    sound("NPC_SScanner.Shoot"),
    sound("NPC_SScanner.Alert"),
    sound("NPC_SScanner.Die"),
    sound("NPC_SScanner.Combat"),
    sound("NPC_SScanner.Idle"),
    sound("NPC_SScanner.Pain"),
    sound("NPC_SScanner.TakePhoto"),
    sound("NPC_SScanner.AttackFlash"),
    sound("NPC_SScanner.DiveBombFlyby"),
    sound("NPC_SScanner.DiveBomb"),
    sound("NPC_SScanner.DeployMine"),
    sound("NPC_SScanner.FlyLoop"),
    includes="combine_mine",
    )
res('npc_zombie',
    mdl("models/zombie/classic.mdl"),
    mdl("models/zombie/classic_torso.mdl"),
    mdl("models/zombie/classic_legs.mdl"),
    sound("Zombie.FootstepRight"),
    sound("Zombie.FootstepLeft"),
    sound("Zombie.FootstepLeft"),
    sound("Zombie.ScuffRight"),
    sound("Zombie.ScuffLeft"),
    sound("Zombie.AttackHit"),
    sound("Zombie.AttackMiss"),
    sound("Zombie.Pain"),
    sound("Zombie.Die"),
    sound("Zombie.Alert"),
    sound("Zombie.Idle"),
    sound("Zombie.Attack"),
    sound("NPC_BaseZombie.Moan1"),
    sound("NPC_BaseZombie.Moan2"),
    sound("NPC_BaseZombie.Moan3"),
    sound("NPC_BaseZombie.Moan4"),
    )
# Actually an alias, but we don't want to swap these.
CLASS_RESOURCES['npc_zombie_torso'] = CLASS_RESOURCES['npc_zombie']

res('npc_fastzombie',
    mdl("models/zombie/fast.mdl"),
    # TODO - Episodic only:
        mdl("models/zombie/Fast_torso.mdl"),
        sound("NPC_FastZombie.CarEnter1"),
        sound("NPC_FastZombie.CarEnter2"),
        sound("NPC_FastZombie.CarEnter3"),
        sound("NPC_FastZombie.CarEnter4"),
        sound("NPC_FastZombie.CarScream"),
    mdl("models/gibs/fast_zombie_torso.mdl"),
    mdl("models/gibs/fast_zombie_legs.mdl"),
    sound("NPC_FastZombie.LeapAttack"),
    sound("NPC_FastZombie.FootstepRight"),
    sound("NPC_FastZombie.FootstepLeft"),
    sound("NPC_FastZombie.AttackHit"),
    sound("NPC_FastZombie.AttackMiss"),
    sound("NPC_FastZombie.LeapAttack"),
    sound("NPC_FastZombie.Attack"),
    sound("NPC_FastZombie.Idle"),
    sound("NPC_FastZombie.AlertFar"),
    sound("NPC_FastZombie.AlertNear"),
    sound("NPC_FastZombie.GallopLeft"),
    sound("NPC_FastZombie.GallopRight"),
    sound("NPC_FastZombie.Scream"),
    sound("NPC_FastZombie.RangeAttack"),
    sound("NPC_FastZombie.Frenzy"),
    sound("NPC_FastZombie.NoSound"),
    sound("NPC_FastZombie.Die"),
    sound("NPC_FastZombie.Gurgle"),
    sound("NPC_FastZombie.Moan1"),
    )
# Actually an alias, but we don't want to swap these.
CLASS_RESOURCES['npc_fastzombie_torso'] = CLASS_RESOURCES['npc_fastzombie']

res('npc_headcrab',
    mdl('models/headcrabclassic.mdl'),
    sound('NPC_HeadCrab.Gib'),
    sound('NPC_HeadCrab.Idle'),
    sound('NPC_HeadCrab.Alert'),
    sound('NPC_HeadCrab.Pain'),
    sound('NPC_HeadCrab.Die'),
    sound('NPC_HeadCrab.Attack'),
    sound('NPC_HeadCrab.Bite'),
    sound('NPC_Headcrab.BurrowIn'),
    sound('NPC_Headcrab.BurrowOut'),
    )

res('npc_headcrab_black',
    mdl('models/headcrabblack.mdl'),

    sound('NPC_BlackHeadcrab.Telegraph'),
    sound('NPC_BlackHeadcrab.Attack'),
    sound('NPC_BlackHeadcrab.Bite'),
    sound('NPC_BlackHeadcrab.Threat'),
    sound('NPC_BlackHeadcrab.Alert'),
    sound('NPC_BlackHeadcrab.Idle'),
    sound('NPC_BlackHeadcrab.Talk'),
    sound('NPC_BlackHeadcrab.AlertVoice'),
    sound('NPC_BlackHeadcrab.Pain'),
    sound('NPC_BlackHeadcrab.Die'),
    sound('NPC_BlackHeadcrab.Impact'),
    sound('NPC_BlackHeadcrab.ImpactAngry'),
    sound('NPC_BlackHeadcrab.FootstepWalk'),
    sound('NPC_BlackHeadcrab.Footstep'),

    sound('NPC_HeadCrab.Gib'),
    sound('NPC_Headcrab.BurrowIn'),
    sound('NPC_Headcrab.BurrowOut'),
    aliases='npc_headcrab_poison',
    )

res('npc_headcrab_fast',
    mdl('models/headcrab.mdl'),
    sound('NPC_FastHeadCrab.Idle'),
    sound('NPC_FastHeadCrab.Alert'),
    sound('NPC_FastHeadCrab.Pain'),
    sound('NPC_FastHeadCrab.Die'),
    sound('NPC_FastHeadCrab.Attack'),
    sound('NPC_FastHeadCrab.Bite'),

    sound('NPC_HeadCrab.Gib'),
    sound('NPC_Headcrab.BurrowIn'),
    sound('NPC_Headcrab.BurrowOut'),
    )

res('npc_heli_avoidbox')
res('npc_heli_avoidsphere')
res('npc_heli_nobomb')
res('npc_helicopter',
    mdl("models/combine_helicopter.mdl"),
    mdl("models/combine_helicopter_broken.mdl"),
    mat("materials/sprites/redglow1.vmt"),
    includes='helicopter_chunk grenade_helicopter',
    )

res('npc_rocket_turret',
    mat('materials/effects/bluelaser1.vmt'),
    mat('materials/sprites/light_glow03.vmt'),
    mdl('models/props_bts/rocket_sentry.mdl'),
    sound('NPC_RocketTurret.LockingBeep'),
    sound('NPC_FloorTurret.LockedBeep'),
    sound('NPC_FloorTurret.RocketFire'),
    includes='rocket_turret_projectile',
    )
res('npc_rollermine',
    mdl("models/roller.mdl"),
    mdl("models/roller_spikes.mdl"),
    mat("materials/sprites/bluelight1.vmt"),
    mat("materials/effects/rollerglow.vmt"),
    mat("materials/sprites/rollermine_shock.vmt"),
    mat("materials/sprites/rollermine_shock_yellow.vmt"),

    sound("NPC_RollerMine.Taunt"),
    sound("NPC_RollerMine.OpenSpikes"),
    sound("NPC_RollerMine.Warn"),
    sound("NPC_RollerMine.Shock"),
    sound("NPC_RollerMine.ExplodeChirp"),
    sound("NPC_RollerMine.Chirp"),
    sound("NPC_RollerMine.ChirpRespond"),
    sound("NPC_RollerMine.ExplodeChirpRespond"),
    sound("NPC_RollerMine.JoltVehicle"),
    sound("NPC_RollerMine.Tossed"),
    sound("NPC_RollerMine.Hurt"),
    sound("NPC_RollerMine.Roll"),
    sound("NPC_RollerMine.RollWithSpikes"),
    sound("NPC_RollerMine.Ping"),
    sound("NPC_RollerMine.Held"),
    sound("NPC_RollerMine.Reprogram"),

    # TODO: Episodic only
    sound("RagdollBoogie.Zap"),
    )

res('npc_vehicledriver',
    'models/roller_vehicledriver.mdl',
    )
