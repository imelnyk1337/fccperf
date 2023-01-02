import ROOT
from ROOT import RDataFrame
import os

ROOT.gSystem.Load("libFCCAnalyses")
ROOT.dummyLoader

ROOT.gInterpreter.Declare(
"""
using namespace FCCAnalyses;
""")

threads = 1
ROOT.EnableImplicitMT(threads)
output_dir = "/home/imelnyk/FCCAnalyses/out_py_standalone/"
output_file = "outputTest.root"
#input_dir = "/tmp/fccperf/p8_ee_ZH_ecm240/"
input_dir = "/home/imelnyk/FCCAnalyses/p8_ee_ZH_ecm240/"
sample_size = 100
is_test = False
test_file = "root://eospublic.cern.ch//eos/experiment/fcc/ee/generation/DelphesEvents/spring2021/IDEA/p8_ee_ZH_ecm240/events_101027117.root"
verbosity = ROOT.Experimental.RLogScopedVerbosity(ROOT.Detail.RDF.RDFLogChannel(), ROOT.Experimental.ELogLevel.kInfo)

def retrieve_data(break_point: int, directory: str) -> ROOT.TChain:
    print(f"Files retrieving starts: {break_point} files are going to be processed")
    root_chain = ROOT.TChain("events")
    current_point = 0
    for filename in os.listdir(directory):
        if current_point == break_point:
            break
        else:
            file = os.path.join(directory, filename)
            if os.path.isfile(file):
                root_chain.Add(str(file))
                current_point += 1
                print(f"File {str(file)} was added to ROOT.TChain object")
    print(f"Files retrieving was finished: {current_point} files had been added")
    return root_chain


def perf():
    root_chain = retrieve_data(sample_size, input_dir)

    df = RDataFrame(root_chain)
    df2 = (df
           .Alias("Muon0", "Muon#0.index")
           .Define("muons", "ReconstructedParticle::get(Muon0, ReconstructedParticles)")
           .Define("selected_muons", "ReconstructedParticle::sel_pt(10.)(muons)")
           .Define("selected_muons_pt", "ReconstructedParticle::get_pt(selected_muons)")
           .Define("selected_muons_y", "ReconstructedParticle::get_y(selected_muons)")
           .Define("selected_muons_p", "ReconstructedParticle::get_p(selected_muons)")
           .Define("selected_muons_e", "ReconstructedParticle::get_e(selected_muons)")
           .Define("zed_leptonic", "ReconstructedParticle::resonanceBuilder(91)(selected_muons)")
           .Define("zed_leptonic_m", "ReconstructedParticle::get_mass(zed_leptonic)")
           .Define("zed_leptonic_pt", "ReconstructedParticle::get_pt(zed_leptonic)")
           .Define("zed_leptonic_recoil", "ReconstructedParticle::recoilBuilder(240)(zed_leptonic)")
           .Define("zed_leptonic_recoil_m", "ReconstructedParticle::get_mass(zed_leptonic_recoil)")
           .Define("zed_leptonic_charge", "ReconstructedParticle::get_charge(zed_leptonic)")
           .Filter("zed_leptonic_recoil_m.size()>0")
           .Snapshot("events", "test_output_py.root", [
		"selected_muons_pt",
            	"selected_muons_y",
            	"selected_muons_p",
            	"selected_muons_e",
            	"zed_leptonic_pt",
            	"zed_leptonic_m",
            	"zed_leptonic_charge",
            	"zed_leptonic_recoil_m"]))


if __name__ == "__main__":
    perf()

