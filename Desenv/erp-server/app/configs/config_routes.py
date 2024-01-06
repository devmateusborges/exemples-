def configure(app):
    # ======
    print(">>>Route configure_auth")
    from ..securities.auth_routes import configure_auth

    configure_auth(app)
    # ======
    print(">>>Route configure_sys")
    from ..modules.sys.base.sys_routes import configure_sys

    configure_sys(app)
    # ======
    print(">>>Route configure_tst")
    from ..modules.tst.base.tst_routes import configure_tst

    configure_tst(app)
    # ======
    print(">>>Route configure_ger")
    from ..modules.ger.base.ger_routes import configure_ger

    configure_ger(app)
    # ======
    print(">>>Route configure_fin")
    from ..modules.fin.base.fin_routes import configure_fin

    configure_fin(app)
    # ======
    print(">>>Route configure_ctb")
    from ..modules.ctb.base.ctb_routes import configure_ctb

    configure_ctb(app)
    # ======
    print(">>>Route configure_fis")
    from ..modules.fis.base.fis_routes import configure_fis

    configure_fis(app)
    # ======
    print(">>>Route configure_bor")
    from ..modules.bor.base.bor_routes import configure_bor

    configure_bor(app)
    # ======
    print(">>>Route configure_pto")
    from ..modules.pto.base.pto_routes import configure_pto

    configure_pto(app)
    # ======
    print(">>>Route configure_rhm")
    from ..modules.rhm.base.rhm_routes import configure_rhm

    configure_rhm(app)
    # ======
    print(">>>Route configure_crm")
    from ..modules.crm.base.crm_routes import configure_crm

    configure_crm(app)
    # ======
    print(">>>Route configure_ope")
    from ..modules.ope.base.ope_routes import configure_ope

    configure_ope(app)
    # ======
    print(">>>Route configure_bov")
    from ..modules.bov.base.bov_routes import configure_bov

    configure_bov(app)
    # ======
    print(">>>Route configure_mov")
    from ..modules.mov.base.mov_routes import configure_mov

    configure_mov(app)
    # ======
    print(">>>Route configure_mob")
    from ..modules.mob.base.mob_routes import configure_mob

    configure_mob(app)
    # ======
    print(">>>Route configure_cms")
    from ..modules.cms.base.cms_routes import configure_cms

    configure_cms(app)
    # ======
    print(">>>Route configure_ind")
    from ..modules.ind.base.ind_routes import configure_ind

    configure_ind(app)
    # ======
