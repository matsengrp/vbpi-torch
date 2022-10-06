import click
import os
import tempfile
import bito

def bito_taxon_order_from_newick_file(newick_path):
    """
    Determines the order of taxa used by bito based on the first tree in the 
    file newick_path. The tree is expected to be in newick format with internal
    and leaf branch lengths plus leaf names only (ete3 format 5). Returned is an
    ordered list of strings of the taxon names.
    """
    with open(newick_path) as the_file:
        first_tree = the_file.readline()
    # After dropping all the parantheses, the taxon start either at the start of
    # the line or after a comma, and end with a colon, but other things also end
    # with a colon. 
    parantheses_removed = first_tree.replace("(","").replace(")","")
    taxon_start_indices = [0]
    taxon_start_indices.extend([j+1 for j in range(len(parantheses_removed)) if parantheses_removed[j]==","])
    taxon_end_indices = [j+parantheses_removed[j:].index(":") for j in taxon_start_indices]
    taxon_order = [ parantheses_removed[start:end] for start, end in zip(taxon_start_indices, taxon_end_indices)  ]
    return taxon_order

@click.command()
@click.argument("newick_path")
@click.argument("fasta_path")
@click.argument("branch_length_path")
@click.argument("taxon_order_path")
def write_average_branch_lengths_to_file(newick_path, fasta_path, branch_length_path, taxon_order_path):
    """
    Read in trees from newick_path associated to sequence data in fasta_path, 
    write out the average branch length (per PCSP or SDAG edge) to 
    branch_length_path, and write out the order of taxon used for bitstrings to
    taxon_order_path.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        bito_data_file = os.path.join(temp_dir, "just_a_name.data")
        all_trees = bito.gp_instance(bito_data_file)
        all_trees.read_newick_file(newick_path)
        all_trees.read_fasta_file(fasta_path)
        all_trees.make_engine()
        all_trees.hot_start_branch_lengths()
        all_trees.branch_lengths_to_csv(branch_length_path)
    with open(taxon_order_path, "w") as the_file:
        the_file.write(str(bito_taxon_order_from_newick_file(newick_path)))
    return None

if __name__=="__main__":
    write_average_branch_lengths_to_file()

