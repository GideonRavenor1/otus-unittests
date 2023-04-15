from factories.base import SortFactory
from factories.insert import InsertionSortFactory
from factories.mege import MergeSortFactory
from factories.selection import SelectionSortFactory

SORT_FACTORIES: dict[str, SortFactory] = {
	"selection": SelectionSortFactory(),
	"merge": MergeSortFactory(),
	"insert": InsertionSortFactory(),
}
