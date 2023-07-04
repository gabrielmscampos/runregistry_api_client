# run attributes:
run_table_attributes = "run_number"

run_triplet_attributes = (
    "castor-castor",
    "cms-cms",
    "csc-csc",
    "ctpps-ctpps",
    "dt-dt",
    "ecal-ecal",
    "ecal-es",
    "hcal-hcal",
    "hlt-hlt",
    "l1t-l1t",
    "l1t-l1tcalo",
    "l1t-l1tmu",
    "lumi-lumi",
    "rpc-rpc",
    "tracker-pixel",
    "tracker-strip",
    # Non global:
    "btag-btag",
    "csc-mep",
    "csc-mem",
    "csc-triggerpe",
    "csc-csctf",
    "csc-ddus",
    "csc-efficiency",
    "csc-gasgains",
    "csc-integrity",
    "csc-timing",
    "csc-strips",
    "csc-resolution",
    "csc-segments",
    "csc-pedestals",
    "csc-occupancy",
    "ctpps-rp56_220",
    "ctpps-rp56_cyl",
    "ctpps-rp56_210",
    "ctpps-rp45_cyl",
    "ctpps-rp45_220",
    "ctpps-rp45_210",
    "ecal-tpg",
    "ecal-timing",
    "ecal-preshower",
    "ecal-noise",
    "ecal-laser",
    "ecal-esp",
    "ecal-esm",
    "ecal-eep",
    "ecal-eem",
    "ecal-ebp",
    "ecal-ebm",
    "ecal-collisions",
    "ecal-analysis",
    "egamma-egamma",
    "egamma-es",
    "hcal-hb",
    "hcal-ho12ls",
    "hcal-ho0ls",
    "hcal-hfls",
    "hcal-hels",
    "hcal-hbls",
    "hcal-ho12",
    "hcal-ho0",
    "hcal-hf",
    "hcal-he",
    "hlt-muons",
    "hlt-electrons",
    "hlt-photons",
    "hlt-jetmet",
    "hlt-tau",
    "hlt-bjets",
    "hlt-technical",
    "hlt-global",
    "jetmet-jetmet",
    "l1t-bptx_tech",
    "l1t-bcs_tech",
    "l1t-hf_tech",
    "l1t-rpc_tech",
    "l1t-software",
    "l1t-muon",
    "l1t-muon_dt",
    "l1t-muon_rpc",
    "l1t-muon_csc",
    "l1t-e_gamma",
    "l1t-jet",
    "l1t-energy_sums",
    "l1t-hf_rings"
    "rpc-elog",
    "rpc-lv",
    "rpc-hv",
    "rpc-feb",
    "rpc-noise",
    "rpc-strip",
    "tau-tau",
)

run_rr_attributes = ("class", "state", "significant", "stop_reason",
                     "short_run")

run_oms_attributes = (
    "energy",
    "l1_key",
    "b_field",
    "hlt_key",
    "l1_menu",
    "l1_rate",
    "end_time",
    "sequence",
    "duration",
    "end_lumi",
    "init_lumi",
    "clock_type",
    "components",
    "run_number",
    "start_time",
    "fill_number",
    "l1_hlt_mode",
    "last_update",
    "ls_duration",
    "stable_beam",
    "hf_included",
    "dt_included",
    "es_included",
    "csc_included",
    "cow_included",
    "daq_included",
    "dcs_included",
    "dqm_included",
    "gem_included",
    "ltc_included",
    "rpc_included",
    "trg_included",
    "trigger_mode",
    "hcal_included",
    "scal_included",
    "efed_included",
    "recorded_lumi",
    "ecal_included",
    "lumi_included",
    "tcds_included",
    "cmssw_version",
    "delivered_lumi",
    "totem_included",
    "tier0_transfer",
    "pixel_included",
    "ctpps_included",
    "hflumi_included",
    "l1_key_stripped",
    "castor_included",
    "hlt_physics_size",
    "fill_type_party2",
    "tracker_included",
    "dt_efed_included",
    "fill_type_party1",
    "injection_scheme",
    "hlt_physics_rate",
    "rpc_efed_included",
    "trg_efed_included",
    "fill_type_runtime",
    "pixel_up_included",
    "csc_efed_included",
    "ctpps_tot_included",
    "ecal_efed_included",
    "hcal_efed_included",
    "l1_triggers_counter",
    "hlt_physics_counter",
    "l1_hlt_mode_stripped",
    "tracker_efed_included",
    "initial_prescale_index",
    "hlt_physics_throughput",
    "beams_present_and_stable",
)

# dataset attributes:
dataset_table_attributes = ("run_number", "dataset_name")

dataset_attributes = ("appeared_in", "global_state", "dt_state", "cms_state",
                      "csc_state", "hlt_state", "l1t_state", "rpc_state",
                      "tau_state", "btag_state", "ecal_state", "hcal_state",
                      "lumi_state", "muon_state", "ctpps_state",
                      "castor_state", "egamma_state", "jetmet_state",
                      "tracker_state")

dataset_triplet_attributes = (
    "dt-dt",
    "csc-tf",
    "rpc-hv",
    "rpc-lv",
    "cms-cms",
    "csc-csc",
    "ecal-es",
    "hcal-hb",
    "hcal-he",
    "hcal-hf",
    "hlt-hlt",
    "hlt-tau",
    "l1t-l1t",
    "rpc-feb",
    "rpc-rpc",
    "tau-tau",
    "ecal-ebm",
    "ecal-ebp",
    "ecal-eem",
    "ecal-eep",
    "ecal-esm",
    "ecal-esp",
    "ecal-tpg",
    "hcal-ho0",
    "rpc-elog",
    "btag-btag",
    "ecal-ecal",
    "hcal-hcal",
    "hcal-ho12",
    "hlt-bjets",
    "hlt-muons",
    "l1t-l1tmu",
    "lumi-lumi",
    "muon-muon",
    "rpc-noise",
    "csc-strips",
    "csc-timing",
    "ecal-laser",
    "ecal-noise",
    "hcal-hb_ls",
    "hcal-he_ls",
    "hcal-hf_ls",
    "hlt-jetmet",
    "ctpps-ctpps",
    "ecal-timing",
    "hcal-hoO_ls",
    "hlt-photons",
    "l1t-e_gamma",
    "l1t-hf_tech",
    "l1t-l1tcalo",
    "l1t-muon_dt",
    "tracker-pix",
    "csc-gasgains",
    "csc-segments",
    "hcal-ho12_ls",
    "l1t-bcs_tech",
    "l1t-hg_rings",
    "l1t-muon_csc",
    "l1t-muon_rpc",
    "l1t-rpc_tech",
    "l1t-software",
    "castor-castor",
    "csc-integrity",
    "csc-occupancy",
    "csc-pedestals",
    "ecal-analysis",
    "egamma-egamma",
    "hlt-electrons",
    "hlt-technical",
    "jetmet-jetmet",
    "l1t-bptx_tech",
    "tracker-strip",
    "tracker-track",
    "csc-efficiency",
    "csc-resolution",
    "csc-triggergpe",
    "ctpps-rp45_220",
    "ctpps-rp45_cyl",
    "ctpps-rp56_210",
    "ctpps-rp56_220",
    "ctpps-rp56_cyl",
    "ecal-preshower",
    "hlt-hlt_global",
    "ecal-collisions",
    "l1t-energy_sums",
    "cms-infrastructure",
)