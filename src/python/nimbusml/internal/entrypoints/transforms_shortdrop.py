# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Transforms.ShortDrop
"""

import numbers

from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def transforms_shortdrop(
        grain_columns,
        data,
        output_data=None,
        model=None,
        min_rows=0,
        **params):
    """
    **Description**
        Drops rows if there aren't enough values per grain.

    :param grain_columns: List of grain columns (inputs).
    :param min_rows: Minimum number of values required (inputs).
    :param data: Input dataset (inputs).
    :param output_data: Transformed dataset (outputs).
    :param model: Transform model (outputs).
    """

    entrypoint_name = 'Transforms.ShortDrop'
    inputs = {}
    outputs = {}

    if grain_columns is not None:
        inputs['GrainColumns'] = try_set(
            obj=grain_columns,
            none_acceptable=False,
            is_of_type=list,
            is_column=True)
    if min_rows is not None:
        inputs['MinRows'] = try_set(
            obj=min_rows,
            none_acceptable=False,
            is_of_type=numbers.Real)
    if data is not None:
        inputs['Data'] = try_set(
            obj=data,
            none_acceptable=False,
            is_of_type=str)
    if output_data is not None:
        outputs['OutputData'] = try_set(
            obj=output_data,
            none_acceptable=False,
            is_of_type=str)
    if model is not None:
        outputs['Model'] = try_set(
            obj=model,
            none_acceptable=False,
            is_of_type=str)

    input_variables = {
        x for x in unlist(inputs.values())
        if isinstance(x, str) and x.startswith("$")}
    output_variables = {
        x for x in unlist(outputs.values())
        if isinstance(x, str) and x.startswith("$")}

    entrypoint = EntryPoint(
        name=entrypoint_name, inputs=inputs, outputs=outputs,
        input_variables=input_variables,
        output_variables=output_variables)
    return entrypoint