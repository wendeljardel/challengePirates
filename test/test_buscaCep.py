import pytest
import os

from src.buscaCep import buildFormData, getDataFromUrl, readDataFromHtmlTable, writeToFile, getPostalCodeInfo, main


def test_buildFormData_whenValidArgs_thenSuccess():
	assert buildFormData('SC', 50) == {
									'UF': 'SC',
									'qtdrow': 51
									}
def test_buildFormData_whenNoLenght_thenUseDefault():
	assert buildFormData('DF') == {
									'UF': 'DF',
									'qtdrow': 101
									}

def test_buildFormData_whenNonPositivoRows_thenAssertionError():
	with pytest.raises(AssertionError) as e_info:
		buildFormData('SC', -2)

def test_buildFormData_whenInvalidRows_thenFail():
	with pytest.raises(AssertionError) as e_info:
		buildFormData('SC', -12)

def test_getDataFromUrl_whenValidFormData_thenSuccess():
	try:
		getDataFromUrl(formData = buildFormData('SP', 100))
	except:
		assert False

def test_readDataFromHtmlTable_whenValidTable_thenSuccess():
	assert 40 == len(
				readDataFromHtmlTable(
					getDataFromUrl(
						formData=buildFormData('SP')
					),
					qtdrow=40
				)
			)

def test_writeToFile_whenValid_thenSuccess(tmp_path):
	writeToFile([{'test': 'content'}], 'test_writeToFile_whenValid_the0/testFile')
	assert (tmp_path / 'testFile.jsonl').exists()
	assert (tmp_path / 'testFile.jsonl').read_text() == '{"test": "content"}' + '\n'

def test_getPostalCodeInfo_whenValid_thenSuccess():
	getPostalCodeInfo(['AC', 'SC'])
	assert os.path.exists('out/AC.jsonl')
	assert os.path.exists('out/SC.jsonl')
	assert len([name for name in os.listdir('./out') if os.path.isfile(os.path.join('./out', name))]) == 2

def test_main():
	main(['PR', 'RS'])
	assert os.path.exists('out/PR.jsonl')
	assert os.path.exists('out/RS.jsonl')
	assert len([name for name in os.listdir('./out') if os.path.isfile(os.path.join('./out', name))]) == 4